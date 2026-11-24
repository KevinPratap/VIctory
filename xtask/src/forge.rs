//! The Forge: `main` plus every open pull request that merges, builds and
//! passes the asset policy, on one branch, with a status page for each pull
//! request. Rules: docs/forge.md.

use std::collections::{BTreeMap, BTreeSet};
use std::path::{Path, PathBuf};

use anyhow::{Context, Result};
use serde::Deserialize;

use crate::gh::{self, cell};

/// `.github/forge.toml`.
#[derive(Deserialize, Default)]
pub struct Config {
    /// The issue where work is claimed (docs/forge.md, "Claims").
    pub coordination_issue: Option<u64>,
    #[serde(default = "fourteen")]
    pub claim_expiry_days: i64,
    #[serde(default)]
    pub hold: Vec<Hold>,
    #[serde(default)]
    pub task: Vec<Task>,
}

fn fourteen() -> i64 {
    14
}

/// A pull request kept out although it builds: observed to break the title.
#[derive(Deserialize)]
pub struct Hold {
    pub pr: u64,
    /// The commit it was seen on (a prefix): a new commit lifts the hold.
    pub head: Option<String>,
    pub reason: String,
}

/// Open work listed in the config (more come from the coordination issue).
#[derive(Deserialize, Clone)]
pub struct Task {
    pub id: String,
    pub what: String,
    #[serde(default, rename = "where")]
    pub place: String,
    #[serde(default)]
    pub needs: String,
}

pub fn config(root: &Path) -> Result<Config> {
    let path = root.join(".github/forge.toml");
    let text =
        std::fs::read_to_string(&path).with_context(|| format!("reading {}", path.display()))?;
    toml::from_str(&text).with_context(|| format!("parsing {}", path.display()))
}

pub struct Opts {
    /// The checkout to build in; it is reset to the forge branch.
    pub repo: PathBuf,
    pub out: PathBuf,
    /// `owner/name` of the repository whose pull requests are taken.
    pub slug: String,
    pub remote: String,
    pub branch: String,
    pub batch: usize,
    pub limit: usize,
    pub tests: bool,
    /// The last run's STATUS.md, for "since the last run".
    pub previous: Option<PathBuf>,
}

struct Pr {
    number: u64,
    draft: bool,
    head: String,
    author: String,
    url: String,
    title: String,
}

#[derive(Clone, Default)]
struct Status {
    result: &'static str,
    files: Vec<String>,
    with: Vec<u64>,
    detail: String,
}

impl Status {
    fn of(result: &'static str) -> Self {
        Status {
            result,
            ..Default::default()
        }
    }
}

struct Run<'a> {
    o: &'a Opts,
    base: String,
    good: String,
    merged: Vec<u64>,
    pending: Vec<(u64, String)>,
    status: BTreeMap<u64, Status>,
    files_of: BTreeMap<u64, BTreeSet<String>>,
}

impl Run<'_> {
    fn git(&self, args: &[&str]) -> Result<gh::Out> {
        gh::run("git", args, &self.o.repo)
    }

    fn head(&self) -> Result<String> {
        Ok(gh::ok("git", &["rev-parse", "HEAD"], &self.o.repo)?
            .trim()
            .to_owned())
    }

    fn reset(&self, to: &str) -> Result<()> {
        gh::ok("git", &["reset", "-q", "--hard", to], &self.o.repo).map(drop)
    }

    fn changed(&mut self, n: u64) -> &BTreeSet<String> {
        let (repo, base) = (&self.o.repo, &self.base);
        self.files_of.entry(n).or_insert_with(|| {
            gh::run(
                "git",
                &[
                    "diff",
                    "--name-only",
                    &format!("{base}...refs/forge/pr/{n}"),
                ],
                repo,
            )
            .map(|o| o.stdout.lines().map(str::to_owned).collect())
            .unwrap_or_default()
        })
    }

    /// Merges pull request `n`; on a conflict, undoes it and returns the files.
    fn merge(&self, n: u64, title: &str) -> Result<Option<Vec<String>>> {
        let msg = format!("Forge: #{n} {title}");
        let r = self.git(&[
            "merge",
            "--no-ff",
            "-q",
            "-m",
            &msg,
            &format!("refs/forge/pr/{n}"),
        ])?;
        if r.ok {
            return Ok(None);
        }
        let files = self
            .git(&["diff", "--name-only", "--diff-filter=U"])?
            .stdout;
        if self.git(&["rev-parse", "-q", "--verify", "MERGE_HEAD"])?.ok {
            self.git(&["merge", "--abort"])?;
        } else {
            self.reset("HEAD")?;
        }
        Ok(Some(files.lines().map(str::to_owned).collect()))
    }

    /// `cargo check` of the whole workspace, then the asset policy.
    fn check(&self) -> Result<Option<String>> {
        let r = gh::run(
            "cargo",
            &[
                "check",
                "--workspace",
                "--all-targets",
                "--message-format=short",
            ],
            &self.o.repo,
        )?;
        if !r.ok {
            let errs: Vec<&str> = r
                .stderr
                .lines()
                .filter(|l| l.contains(": error") || l.starts_with("error"))
                .take(2)
                .collect();
            return Ok(Some(errs.join(" / ")));
        }
        let (_, found) = crate::policy::violations(&self.o.repo, false)?;
        if !found.is_empty() {
            return Ok(Some(format!(
                "asset policy: {}",
                found[..found.len().min(3)].join("; ")
            )));
        }
        Ok(None)
    }

    fn settle(&mut self) -> Result<()> {
        if self.pending.is_empty() {
            return Ok(());
        }
        let batch = std::mem::take(&mut self.pending);
        match self.check()? {
            None => self.keep(&batch)?,
            Some(err) => {
                println!("a batch of {} fails; halving it", batch.len());
                let good = self.good.clone();
                self.reset(&good)?;
                self.bisect(&batch, err)?;
            }
        }
        Ok(())
    }

    fn keep(&mut self, batch: &[(u64, String)]) -> Result<()> {
        self.good = self.head()?;
        for (n, _) in batch {
            self.merged.push(*n);
            self.status.insert(*n, Status::of("in forge"));
        }
        println!("{} in the branch", self.merged.len());
        Ok(())
    }

    /// Takes what builds of `batch`, halving a failing part until the pull
    /// request that breaks it is alone (`err`: the whole part's error).
    fn bisect(&mut self, batch: &[(u64, String)], err: String) -> Result<()> {
        if let [(n, _)] = batch {
            println!("#{n} fails: {err}");
            self.status.insert(
                *n,
                Status {
                    detail: err,
                    ..Status::of("breaks the build")
                },
            );
            return Ok(());
        }
        let (a, b) = batch.split_at(batch.len() / 2);
        for part in [a, b] {
            let mut kept = Vec::new();
            for (n, t) in part {
                if self.merge(*n, t)?.is_none() {
                    kept.push((*n, t.clone()));
                } else {
                    self.status
                        .insert(*n, Status::of("conflicts with pull requests"));
                }
            }
            if kept.is_empty() {
                continue;
            }
            match self.check()? {
                None => self.keep(&kept)?,
                Some(err) => {
                    let good = self.good.clone();
                    self.reset(&good)?;
                    self.bisect(&kept, err)?;
                }
            }
        }
        Ok(())
    }
}

pub fn run(o: &Opts, cfg: &Config) -> Result<()> {
    std::fs::create_dir_all(&o.out)?;
    let list = gh::ok(
        "gh",
        &[
            "pr",
            "list",
            "-R",
            &o.slug,
            "--state",
            "open",
            "--limit",
            "5000",
            "--json",
            "number,isDraft,headRefOid,author,url,title",
            "--jq",
            ".[] | [.number, .isDraft, .headRefOid, .author.login, .url, .title] | @tsv",
        ],
        &o.repo,
    )?;
    let mut prs: Vec<Pr> = list
        .lines()
        .filter_map(|l| {
            let f = gh::tsv(l);
            Some(Pr {
                number: f.first()?.parse().ok()?,
                draft: f.get(1)? == "true",
                head: f.get(2)?.clone(),
                author: f.get(3)?.clone(),
                url: f.get(4)?.clone(),
                title: f.get(5).cloned().unwrap_or_default(),
            })
        })
        .collect();
    prs.sort_by_key(|p| p.number);
    if o.limit > 0 {
        prs.truncate(o.limit);
    }
    println!("{} open pull requests", prs.len());

    gh::ok("git", &["fetch", "-q", &o.remote, "main"], &o.repo)?;
    let base = gh::ok(
        "git",
        &["rev-parse", &format!("{}/main", o.remote)],
        &o.repo,
    )?
    .trim()
    .to_owned();
    for chunk in prs.chunks(100) {
        let specs: Vec<String> = chunk
            .iter()
            .map(|p| format!("+refs/pull/{0}/head:refs/forge/pr/{0}", p.number))
            .collect();
        let mut args = vec!["fetch", "-q", o.remote.as_str()];
        args.extend(specs.iter().map(String::as_str));
        let f = gh::run("git", &args, &o.repo)?;
        if !f.ok {
            println!("fetch: {}", f.stderr.trim());
        }
    }

    let mut r = Run {
        o,
        base: base.clone(),
        good: base.clone(),
        merged: Vec::new(),
        pending: Vec::new(),
        status: BTreeMap::new(),
        files_of: BTreeMap::new(),
    };
    let mut todo = Vec::new();
    for p in &prs {
        let pr_ref = format!("refs/forge/pr/{}", p.number);
        let held = cfg
            .hold
            .iter()
            .find(|h| h.pr == p.number && h.head.as_deref().is_none_or(|c| p.head.starts_with(c)));
        let s = if !r.git(&["rev-parse", "-q", "--verify", &pr_ref])?.ok {
            Status::of("not fetched")
        } else if p.draft {
            Status::of("draft")
        } else if let Some(h) = held {
            Status {
                detail: h.reason.clone(),
                ..Status::of("held")
            }
        } else {
            let mt = r.git(&[
                "merge-tree",
                "--write-tree",
                "--name-only",
                "--no-messages",
                &base,
                &pr_ref,
            ])?;
            let workflows: Vec<String> = r
                .changed(p.number)
                .iter()
                .filter(|f| f.starts_with(".github/workflows/"))
                .take(5)
                .cloned()
                .collect();
            match mt.code {
                // The Actions token cannot push workflow changes, and the
                // Forge does not run other people's CI changes unreviewed.
                Some(0) if !workflows.is_empty() => Status {
                    files: workflows,
                    ..Status::of("changes CI workflows")
                },
                Some(0) => {
                    todo.push(p);
                    continue;
                }
                Some(1) => Status {
                    files: mt
                        .stdout
                        .lines()
                        .skip(1)
                        .take(5)
                        .map(str::to_owned)
                        .collect(),
                    ..Status::of("conflicts with main")
                },
                _ => Status {
                    detail: mt.stderr.trim().to_owned(),
                    ..Status::of("error")
                },
            }
        };
        r.status.insert(p.number, s);
    }
    println!("{} merge with main", todo.len());

    gh::ok("git", &["checkout", "-q", "-B", &o.branch, &base], &o.repo)?;
    for p in todo {
        match r.merge(p.number, &p.title)? {
            None => {
                r.pending.push((p.number, p.title.clone()));
                if r.pending.len() >= o.batch {
                    r.settle()?;
                }
            }
            Some(files) => {
                // Conflicts here but not with main: with what is already in.
                let taken: Vec<u64> = r
                    .merged
                    .iter()
                    .chain(r.pending.iter().map(|(n, _)| n))
                    .copied()
                    .collect();
                let mut with = Vec::new();
                for m in taken {
                    if files.iter().any(|f| r.changed(m).contains(f)) {
                        with.push(m);
                    }
                }
                with.truncate(8);
                r.status.insert(
                    p.number,
                    Status {
                        files: files.into_iter().take(5).collect(),
                        with,
                        ..Status::of("conflicts with pull requests")
                    },
                );
            }
        }
    }
    r.settle()?;
    let good = r.good.clone();
    r.reset(&good)?;
    println!("{} pull requests in {} at {good}", r.merged.len(), o.branch);

    let tests = if o.tests {
        Some(workspace_tests(&o.repo)?)
    } else {
        None
    };
    let previous: BTreeSet<u64> = o
        .previous
        .as_ref()
        .and_then(|p| std::fs::read_to_string(p).ok())
        .map(|t| in_forge(&t))
        .unwrap_or_default();
    let md = page(
        o,
        &prs,
        &r,
        &good,
        tests.as_ref(),
        (!previous.is_empty()).then_some(&previous),
    );
    std::fs::write(o.out.join("STATUS.md"), md)?;
    println!("wrote {}", o.out.join("STATUS.md").display());
    Ok(())
}

struct Tests {
    passed: u64,
    failed: u64,
    ignored: u64,
    failing: BTreeSet<String>,
}

fn workspace_tests(repo: &Path) -> Result<Tests> {
    let r = gh::run("cargo", &["test", "--workspace", "--no-fail-fast"], repo)?;
    let out = format!("{}{}", r.stdout, r.stderr);
    let count = |word: &str| -> u64 {
        out.lines()
            .filter(|l| l.starts_with("test result:"))
            .filter_map(|l| {
                let i = l.find(&format!(" {word}"))?;
                l[..i]
                    .rsplit(|c: char| !c.is_ascii_digit())
                    .next()?
                    .parse::<u64>()
                    .ok()
            })
            .sum()
    };
    let failing = out
        .lines()
        .filter_map(|l| {
            l.strip_prefix("test ")?
                .strip_suffix(" ... FAILED")
                .map(str::to_owned)
        })
        .collect();
    Ok(Tests {
        passed: count("passed"),
        failed: count("failed"),
        ignored: count("ignored"),
        failing,
    })
}

/// The pull requests a STATUS.md lists under "in forge".
fn in_forge(md: &str) -> BTreeSet<u64> {
    let mut on = false;
    let mut set = BTreeSet::new();
    for l in md.lines() {
        if l.starts_with("## ") {
            on = l.starts_with("## in forge");
        } else if on
            && let Some(rest) = l.strip_prefix("| [#")
            && let Some(n) = rest.split(']').next().and_then(|n| n.parse().ok())
        {
            set.insert(n);
        }
    }
    set
}

const ORDER: [&str; 10] = [
    "in forge",
    "conflicts with pull requests",
    "conflicts with main",
    "breaks the build",
    "changes CI workflows",
    "held",
    "draft",
    "not fetched",
    "error",
    "?",
];

fn page(
    o: &Opts,
    prs: &[Pr],
    r: &Run,
    good: &str,
    tests: Option<&Tests>,
    previous: Option<&BTreeSet<u64>>,
) -> String {
    let mut by: BTreeMap<usize, Vec<(&Pr, Status)>> = BTreeMap::new();
    for p in prs {
        let s = r
            .status
            .get(&p.number)
            .cloned()
            .unwrap_or_else(|| Status::of("?"));
        let k = ORDER
            .iter()
            .position(|x| *x == s.result)
            .unwrap_or(ORDER.len() - 1);
        by.entry(k).or_default().push((p, s));
    }
    let mut md = vec![
        "# Forge status".to_owned(),
        String::new(),
        format!(
            "Generated {} UTC. Base: `main` at `{}`. Branch `{}` at `{}`: **{} of {} open pull requests** \
             merged, building (`cargo check --workspace --all-targets`) and passing the asset policy. \
             Rules: [docs/forge.md](https://github.com/{}/blob/main/docs/forge.md).",
            gh::date(gh::now()),
            &r.base[..10.min(r.base.len())],
            o.branch,
            &good[..10.min(good.len())],
            r.merged.len(),
            prs.len(),
            o.slug,
        ),
        String::new(),
        "| Result | Pull requests |".to_owned(),
        "|---|---:|".to_owned(),
    ];
    for (k, v) in &by {
        md.push(format!("| {} | {} |", ORDER[*k], v.len()));
    }
    md.push(String::new());
    if let Some(t) = tests {
        md.push("## Tests on the branch".to_owned());
        md.push(String::new());
        md.push(format!(
            "`cargo test --workspace --no-fail-fast`: **{} passed, {} failed, {} ignored** (where the Forge ran; \
             GPU tests skip without a GPU). Failing tests do not keep a pull request out; they are listed for the authors.",
            t.passed, t.failed, t.ignored
        ));
        md.push(String::new());
        md.extend(t.failing.iter().map(|f| format!("- `{f}`")));
        md.push(String::new());
    }
    if let Some(prev) = previous {
        let now: BTreeSet<u64> = r.merged.iter().copied().collect();
        let list = |s: Vec<&u64>| {
            if s.is_empty() {
                "none".to_owned()
            } else {
                s.iter()
                    .map(|n| format!("#{n}"))
                    .collect::<Vec<_>>()
                    .join(", ")
            }
        };
        md.push("## Since the last run".to_owned());
        md.push(String::new());
        md.push(format!(
            "Joined the branch: {}.",
            list(now.difference(prev).collect())
        ));
        md.push(String::new());
        md.push(format!(
            "Left the branch (closed, merged into `main`, or now conflicting or failing): {}.",
            list(prev.difference(&now).collect())
        ));
        md.push(String::new());
    }
    for (k, v) in &by {
        md.push(format!("## {} ({})", ORDER[*k], v.len()));
        md.push(String::new());
        md.push("| PR | Title | Author | Detail |".to_owned());
        md.push("|---|---|---|---|".to_owned());
        for (p, s) in v {
            let mut d = String::new();
            if !s.files.is_empty() {
                d += &format!(
                    "files: {}",
                    s.files
                        .iter()
                        .map(|f| format!("`{f}`"))
                        .collect::<Vec<_>>()
                        .join(", ")
                );
            }
            if !s.with.is_empty() {
                d += &format!(
                    "; with {}",
                    s.with
                        .iter()
                        .map(|n| format!("#{n}"))
                        .collect::<Vec<_>>()
                        .join(", ")
                );
            }
            d += &s.detail;
            md.push(format!(
                "| [#{}]({}) | {} | {} | {} |",
                p.number,
                p.url,
                cell(&p.title),
                p.author,
                cell(&d)
            ));
        }
        md.push(String::new());
    }
    md.join("\n")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_status_page_lists_its_branch() {
        let md = "# x\n\n## in forge (2)\n\n| PR |\n|---|\n| [#12](u) | a |\n| [#30](u) | b |\n\n## draft (1)\n\n| [#40](u) | c |\n";
        assert_eq!(in_forge(md), BTreeSet::from([12, 30]));
    }

    #[test]
    fn the_config_reads_holds_and_tasks() {
        let c: Config = toml::from_str(
            "coordination_issue = 7\n[[hold]]\npr = 3\nhead = \"abc\"\nreason = \"r\"\n\
             [[task]]\nid = \"A-1\"\nwhat = \"w\"\nwhere = \"x\"\n",
        )
        .unwrap();
        assert_eq!(
            (c.coordination_issue, c.claim_expiry_days, c.hold.len()),
            (Some(7), 14, 1)
        );
        assert_eq!(
            (c.task[0].id.as_str(), c.task[0].place.as_str()),
            ("A-1", "x")
        );
    }
}

//! Claims: who works on what, from the coordination issue (docs/forge.md,
//! "Claims"). Reads the issue's table and comments, writes CLAIMS.md, and
//! with `--comment` keeps one bot comment in the issue current (it edits
//! only that comment).

use std::collections::BTreeMap;
use std::path::Path;

use anyhow::{Context, Result, bail};

use crate::forge::{Config, Task};
use crate::gh::{self, cell};

/// Marks the bot's own comment, so it is found again and never read as claims.
const MARK: &str = "<!-- forge-claims -->";

struct Comment {
    id: u64,
    user: String,
    at: i64,
    edited: bool,
    url: String,
    body: String,
}

struct Holder {
    user: String,
    at: i64,
    url: String,
}

struct Pr {
    author: String,
    state: String,
    url: String,
    text: String,
}

pub fn run(root: &Path, slug: &str, cfg: &Config, out: &Path, comment: bool) -> Result<()> {
    let Some(issue) = cfg.coordination_issue else {
        bail!("no coordination_issue in .github/forge.toml");
    };
    let expire = cfg.claim_expiry_days * 86_400;
    let now = gh::now();

    let mut comments: Vec<Comment> = gh::ok(
        "gh",
        &[
            "api",
            "--paginate",
            &format!("repos/{slug}/issues/{issue}/comments?per_page=100"),
            "--jq",
            ".[] | [.id, .user.login, .created_at, .updated_at, .html_url, .body] | @tsv",
        ],
        root,
    )?
    .lines()
    .filter_map(|l| {
        let f = gh::tsv(l);
        let (at, upd) = (gh::unix(f.get(2)?), gh::unix(f.get(3)?));
        Some(Comment {
            id: f.first()?.parse().ok()?,
            user: f.get(1)?.clone(),
            at,
            edited: upd - at > 60,
            url: f.get(4)?.clone(),
            body: f.get(5).cloned().unwrap_or_default(),
        })
    })
    .collect();
    comments.sort_by_key(|c| c.id);
    let body = gh::ok(
        "gh",
        &[
            "api",
            &format!("repos/{slug}/issues/{issue}"),
            "--jq",
            ".body // \"\"",
        ],
        root,
    )?;
    let prs: BTreeMap<u64, Pr> = gh::ok(
        "gh",
        &[
            "pr",
            "list",
            "-R",
            slug,
            "--state",
            "all",
            "--limit",
            "5000",
            "--json",
            "number,author,state,url,title,body",
            "--jq",
            ".[] | [.number, .author.login, .state, .url, .title + \" \" + (.body // \"\")] | @tsv",
        ],
        root,
    )?
    .lines()
    .filter_map(|l| {
        let f = gh::tsv(l);
        Some((
            f.first()?.parse().ok()?,
            Pr {
                author: f.get(1)?.clone(),
                state: f.get(2)?.clone(),
                url: f.get(3)?.clone(),
                text: f.get(4).cloned().unwrap_or_default().to_uppercase(),
            },
        ))
    })
    .collect();

    // Tasks: the config, then the issue's table (| `ID` | what | where | needs |).
    let mut tasks: BTreeMap<String, Task> = BTreeMap::new();
    let mut order: Vec<String> = Vec::new();
    let mut add = |t: Task, tasks: &mut BTreeMap<String, Task>| {
        if !tasks.contains_key(&t.id) {
            order.push(t.id.clone());
            tasks.insert(t.id.clone(), t);
        }
    };
    for t in &cfg.task {
        add(
            Task {
                id: t.id.to_uppercase(),
                ..t.clone()
            },
            &mut tasks,
        );
    }
    for line in body.lines() {
        let cols: Vec<&str> = line
            .trim()
            .trim_matches('|')
            .split('|')
            .map(str::trim)
            .collect();
        if let Some(id) = cols
            .first()
            .and_then(|c| c.strip_prefix('`')?.strip_suffix('`'))
            && is_id(id)
            && cols.len() >= 2
        {
            let get = |i: usize| cols.get(i).map_or(String::new(), |s| (*s).to_owned());
            add(
                Task {
                    id: id.to_uppercase(),
                    what: get(1),
                    place: get(2),
                    needs: get(3),
                },
                &mut tasks,
            );
        }
    }

    let mut claims: BTreeMap<String, Holder> = BTreeMap::new();
    let mut waiting: BTreeMap<String, Vec<Holder>> = BTreeMap::new();
    let mut done: BTreeMap<String, u64> = BTreeMap::new();
    let mut problems = Vec::new();
    let (mut new_n, mut find_n) = (0, 0);
    for c in comments.iter().filter(|c| !c.body.contains(MARK)) {
        for line in c.body.lines() {
            let Some((cmd, arg)) = command(line) else {
                continue;
            };
            if c.edited && cmd != "finding" {
                problems.push(format!("[comment]({}) by @{}: edited after posting, so its `{cmd}` does not count; post a new comment.", c.url, c.user));
                continue;
            }
            if cmd == "finding" {
                find_n += 1;
                let id = format!("FIND-{find_n}");
                add(
                    Task {
                        id,
                        what: format!("{arg} ([finding]({}) by @{})", c.url, c.user),
                        place: String::new(),
                        needs: String::new(),
                    },
                    &mut tasks,
                );
                continue;
            }
            let ids: Vec<String> = arg
                .split("->")
                .next()
                .unwrap_or("")
                .split(',')
                .filter_map(|p| p.split_whitespace().next())
                .map(|w| w.trim_matches('`').to_uppercase())
                .collect();
            match cmd {
                "claiming" => {
                    let mut listed: Vec<String> = ids
                        .iter()
                        .filter(|i| tasks.contains_key(*i))
                        .cloned()
                        .collect();
                    if listed.is_empty() && !ids.iter().any(|i| is_id(i)) {
                        new_n += 1;
                        let id = format!("NEW-{new_n}");
                        add(
                            Task {
                                id: id.clone(),
                                what: format!("{arg} ([claim]({}) by @{})", c.url, c.user),
                                place: String::new(),
                                needs: String::new(),
                            },
                            &mut tasks,
                        );
                        listed.push(id);
                    }
                    for i in ids.iter().filter(|i| is_id(i) && !tasks.contains_key(*i)) {
                        problems.push(format!("[comment]({}) by @{}: `{i}` is not a task; use `claiming: <one line>` for something new.", c.url, c.user));
                    }
                    for id in listed {
                        if done.contains_key(&id) {
                            continue;
                        }
                        match claims.get(&id) {
                            Some(h) if h.user != c.user => {
                                let w = waiting.entry(id).or_default();
                                if !w.iter().any(|x| x.user == c.user) {
                                    w.push(Holder {
                                        user: c.user.clone(),
                                        at: c.at,
                                        url: c.url.clone(),
                                    });
                                }
                            }
                            _ => {
                                claims.insert(
                                    id,
                                    Holder {
                                        user: c.user.clone(),
                                        at: c.at,
                                        url: c.url.clone(),
                                    },
                                );
                            }
                        }
                    }
                }
                "done" => {
                    let Some(id) = ids.first() else { continue };
                    let pr = arg
                        .split('#')
                        .nth(1)
                        .and_then(|s| s.split(|c: char| !c.is_ascii_digit()).next()?.parse().ok());
                    match (claims.get(id), pr) {
                        (Some(h), Some(n)) if h.user == c.user => {
                            done.insert(id.clone(), n);
                        }
                        (Some(h), None) if h.user == c.user => problems.push(format!(
                            "[comment]({}) by @{}: `done: {id}` names no pull request (`-> #123`).",
                            c.url, c.user
                        )),
                        _ => problems.push(format!(
                            "[comment]({}) by @{}: `done: {id}` without holding the claim.",
                            c.url, c.user
                        )),
                    }
                }
                _ => {
                    for id in &ids {
                        if claims.get(id).is_some_and(|h| h.user == c.user) {
                            claims.remove(id);
                            done.remove(id);
                            if let Some(w) = waiting.get_mut(id)
                                && !w.is_empty()
                            {
                                let next = w.remove(0);
                                claims.insert(id.clone(), Holder { at: c.at, ..next });
                            }
                        }
                    }
                }
            }
        }
    }
    // A holder's own open pull request naming the task counts as `done`.
    for (id, h) in &claims {
        if !done.contains_key(id)
            && let Some((n, _)) = prs.iter().find(|(_, p)| {
                p.author == h.user && p.state == "OPEN" && p.text.contains(id.as_str())
            })
        {
            done.insert(id.clone(), *n);
        }
    }
    // An expired claim passes to the next in line, from the day it expired.
    for (id, h) in claims.iter_mut() {
        while !done.contains_key(id) && now - h.at >= expire {
            let Some(w) = waiting.get_mut(id).filter(|w| !w.is_empty()) else {
                break;
            };
            let next = w.remove(0);
            let at = next.at.max(h.at + expire);
            *h = Holder { at, ..next };
        }
    }

    let state = |id: &str| -> (&'static str, String) {
        if let Some(n) = done.get(id) {
            let holder = claims.get(id).map_or("?", |h| h.user.as_str());
            return match prs.get(n).map(|p| p.state.as_str()) {
                Some("MERGED") => ("merged", format!("#{n} merged")),
                Some("CLOSED") => ("open", format!("#{n} closed; free again")),
                _ => (
                    "in review",
                    match prs.get(n) {
                        Some(p) => format!("[#{n}]({}) by @{holder}", p.url),
                        None => format!("#{n} by @{holder}"),
                    },
                ),
            };
        }
        match claims.get(id) {
            Some(h) if now - h.at >= expire => ("open", format!("claim by @{} expired", h.user)),
            Some(h) => {
                let w = waiting
                    .get(id)
                    .filter(|w| !w.is_empty())
                    .map_or(String::new(), |w| {
                        format!(
                            "; waiting: {}",
                            w.iter()
                                .map(|x| format!("@{}", x.user))
                                .collect::<Vec<_>>()
                                .join(", ")
                        )
                    });
                (
                    "claimed",
                    format!(
                        "@{} since {} ([claim]({})){w}",
                        h.user,
                        &gh::date(h.at)[..10],
                        h.url
                    ),
                )
            }
            None => ("open", String::new()),
        }
    };
    let rank = |s: &str| {
        ["open", "claimed", "in review", "merged"]
            .iter()
            .position(|x| *x == s)
            .unwrap_or(4)
    };
    let mut rows: Vec<(String, &Task, &'static str, String)> = order
        .iter()
        .map(|id| {
            let (s, w) = state(id);
            (id.clone(), &tasks[id], s, w)
        })
        .collect();
    rows.sort_by(|a, b| {
        rank(a.2)
            .cmp(&rank(b.2))
            .then_with(|| natural(&a.0).cmp(&natural(&b.0)))
    });

    let head = format!(
        "Who works on what, from the comments in #{issue}. Rules: [docs/forge.md](https://github.com/{slug}/blob/main/docs/forge.md#claims). \
         **Before you write code**, comment `claiming: <ID>` there (or `claiming: <one line>` for something new); \
         when your pull request is open, `done: <ID> -> #<PR>` (or put the ID in the pull request); \
         `finding: <one line>` adds a task."
    );
    let mut md = vec![
        "# Claims".to_owned(),
        String::new(),
        head.clone(),
        String::new(),
        "| ID | Status | What | Where | Needs | Holder / pull request |".to_owned(),
        "|---|---|---|---|---|---|".to_owned(),
    ];
    for (id, t, s, w) in &rows {
        md.push(format!(
            "| `{id}` | {s} | {} | {} | {} | {} |",
            cell(&t.what),
            cell(&t.place),
            cell(&t.needs),
            cell(w)
        ));
    }
    if !problems.is_empty() {
        md.push(String::new());
        md.push("## Not accepted".to_owned());
        md.push(String::new());
        md.extend(problems.iter().map(|p| format!("- {p}")));
    }
    md.push(String::new());
    std::fs::create_dir_all(out)?;
    std::fs::write(out.join("CLAIMS.md"), md.join("\n"))?;
    println!(
        "{} tasks, {} claims, {} not accepted",
        rows.len(),
        claims.len(),
        problems.len()
    );

    if comment {
        // The roster in the issue: everything not merged yet, short.
        let mut c = vec![
            MARK.to_owned(),
            "## Claims".to_owned(),
            String::new(),
            head,
            String::new(),
            "| ID | Status | What | Holder / pull request |".to_owned(),
            "|---|---|---|---|".to_owned(),
        ];
        for (id, t, s, w) in rows.iter().filter(|r| r.2 != "merged") {
            let what: String = t.what.chars().take(90).collect();
            let more = if t.what.chars().count() > 90 {
                "…"
            } else {
                ""
            };
            c.push(format!(
                "| `{id}` | {s} | {}{more} | {} |",
                cell(&what),
                cell(w)
            ));
        }
        if !problems.is_empty() {
            c.push(String::new());
            c.push(format!("{} comment(s) not accepted: see the full list in CLAIMS.md on the `forge/status` branch.", problems.len()));
        }
        c.push(String::new());
        c.push(format!(
            "_Updated {} UTC by the claims workflow; it edits only this comment._",
            gh::date(now)
        ));
        let text = c.join("\n");
        let mine = comments
            .iter()
            .find(|c| c.body.contains(MARK))
            .map(|c| c.id);
        let previous = comments
            .iter()
            .find(|c| c.body.contains(MARK))
            .map(|c| strip_stamp(&c.body));
        if previous.as_deref() == Some(strip_stamp(&text).as_str()) {
            println!("bot comment unchanged");
            return Ok(());
        }
        let file = out.join("claims-comment.md");
        std::fs::write(&file, &text)?;
        let body_arg = format!("body=@{}", file.display());
        match mine {
            Some(id) => gh::ok(
                "gh",
                &[
                    "api",
                    "-X",
                    "PATCH",
                    &format!("repos/{slug}/issues/comments/{id}"),
                    "-F",
                    &body_arg,
                ],
                root,
            ),
            None => gh::ok(
                "gh",
                &[
                    "api",
                    &format!("repos/{slug}/issues/{issue}/comments"),
                    "-F",
                    &body_arg,
                ],
                root,
            ),
        }
        .context("updating the claims comment")?;
        println!("bot comment updated");
    }
    Ok(())
}

/// A `claiming:` / `done:` / `release:` / `finding:` line: (command, argument).
fn command(line: &str) -> Option<(&'static str, String)> {
    let l = line.trim().trim_start_matches(['-', '*']).trim();
    let (cmd, arg) = l.split_once(':')?;
    let cmd = match cmd.trim().to_lowercase().as_str() {
        "claiming" => "claiming",
        "done" => "done",
        "release" => "release",
        "finding" => "finding",
        _ => return None,
    };
    let arg = arg.trim();
    (!arg.is_empty()).then(|| (cmd, arg.to_owned()))
}

/// `AREA-NAME`: letters first, then dash-separated parts.
fn is_id(s: &str) -> bool {
    let mut parts = s.split('-');
    parts.next().is_some_and(|p| {
        p.chars().next().is_some_and(|c| c.is_ascii_alphabetic())
            && p.chars().all(|c| c.is_ascii_alphanumeric())
    }) && s.contains('-')
        && parts.all(|p| !p.is_empty() && p.chars().all(|c| c.is_ascii_alphanumeric()))
}

fn natural(s: &str) -> Vec<(String, u64)> {
    let mut v = Vec::new();
    let (mut text, mut num) = (String::new(), String::new());
    for c in s.chars() {
        if c.is_ascii_digit() {
            num.push(c);
        } else {
            if !num.is_empty() {
                v.push((std::mem::take(&mut text), num.parse().unwrap_or(0)));
                num.clear();
            }
            text.push(c);
        }
    }
    v.push((text, num.parse().unwrap_or(0)));
    v
}

fn strip_stamp(s: &str) -> String {
    s.lines()
        .filter(|l| !l.starts_with("_Updated "))
        .collect::<Vec<_>>()
        .join("\n")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn commands_are_read_from_lines() {
        assert_eq!(
            command("claiming: GPU-X"),
            Some(("claiming", "GPU-X".to_owned()))
        );
        assert_eq!(
            command("- Done: GPU-X -> #12"),
            Some(("done", "GPU-X -> #12".to_owned()))
        );
        assert_eq!(command("finding:   "), None);
        assert_eq!(command("note: hello"), None);
    }

    #[test]
    fn task_ids_need_a_dash() {
        assert!(is_id("GPU-BLACK-WORLD") && is_id("find-12"));
        assert!(!is_id("GPU") && !is_id("1-A") && !is_id("A--B") && !is_id("the"));
    }

    #[test]
    fn ids_sort_by_their_numbers() {
        let mut v = vec!["FIND-10", "FIND-2", "A-1"];
        v.sort_by_key(|s| natural(s));
        assert_eq!(v, ["A-1", "FIND-2", "FIND-10"]);
    }
}

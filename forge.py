"""VIctory Forge: upstream main plus every open pull request that merges and builds.

Builds one branch anyone can test, and a status page saying, for each open
pull request, whether it is in that branch, which file it conflicts on (and
with which merged pull requests), or what it breaks.

Usage (from anywhere; needs git >= 2.38, gh, cargo):
    python -I forge.py --repo <VIctory worktree> --out <status folder>
        [--upstream Marvisak/VIctory] [--remote origin] [--branch forge/main]
        [--batch 20] [--held held.json] [--limit N] [--tests] [--previous status.json]
        [--tested-branch forge/tested] [--diagnostic-runs 6] [--diagnostic-seconds 900]

--tests runs `cargo test --workspace --no-fail-fast` on the final branch and
reports it; --previous names the last run's status.json, to list what changed.

The worktree is reset to the forge branch: use a worktree of its own.
Nothing from any game is read or written; only the repository's code.
"""
import argparse, datetime, json, os, subprocess, sys, time

ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--upstream", default="Marvisak/VIctory")
ap.add_argument("--remote", default="origin")
ap.add_argument("--branch", default="forge/main")
ap.add_argument("--batch", type=int, default=20)
ap.add_argument("--held", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "held.json"))
ap.add_argument("--limit", type=int, default=0, help="only the first N pull requests (testing)")
ap.add_argument("--tests", action="store_true", help="run the workspace tests on the final branch")
ap.add_argument("--tested-branch", help="advance this branch only after baseline regression checks (requires --tests)")
ap.add_argument("--test-timeout", type=int, default=1800, help="seconds per baseline/candidate test run")
ap.add_argument("--diagnostic-runs", type=int, default=6, help="maximum regression-isolation probes")
ap.add_argument("--diagnostic-seconds", type=int, default=900, help="total seconds for isolation probes")
ap.add_argument("--previous", help="the last run's status.json, to report what changed")
a = ap.parse_args()
if a.tested_branch and not a.tests:
    ap.error("--tested-branch requires --tests")
if a.tested_branch == a.branch:
    ap.error("--tested-branch must differ from the candidate branch")
if a.test_timeout <= 0 or a.diagnostic_runs < 0 or a.diagnostic_seconds < 0:
    ap.error("test timeout must be positive and diagnostic budgets nonnegative")
os.makedirs(a.out, exist_ok=True)
LOG = open(os.path.join(a.out, "forge.log"), "a", encoding="utf-8")


def log(*m):
    line = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in m)
    print(line, flush=True)
    LOG.write(line + "\n")
    LOG.flush()


def git(*args, check=False):
    r = subprocess.run(["git", *args], cwd=a.repo, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r


def cargo_check():
    r = subprocess.run(["cargo", "check", "--workspace", "--all-targets", "--message-format=short"],
                       cwd=a.repo, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=3600)
    errs = [l.strip() for l in r.stderr.splitlines() if ": error" in l or l.startswith("error")]
    if r.returncode:
        return False, errs[:3]
    # The repository's own asset policy: nothing from the game may be
    # committed, so a pull request adding what it refuses stays out.
    p = subprocess.run(["cargo", "run", "-q", "-p", "xtask", "--", "policy"],
                       cwd=a.repo, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=3600)
    if p.returncode:
        found = [l.strip() for l in (p.stdout + p.stderr).splitlines() if l.startswith("POLICY")]
        return False, ["asset policy: " + "; ".join(found[:3])]
    return True, []


held = {}
if os.path.exists(a.held):
    held = {int(k): v for k, v in json.load(open(a.held, encoding="utf-8")).items()}

# Open pull requests.
r = subprocess.run(["gh", "pr", "list", "-R", a.upstream, "--state", "open", "--limit", "3000",
                    "--json", "number,title,author,isDraft,headRefOid,updatedAt,url"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode:
    sys.exit(r.stderr)
prs = sorted(json.loads(r.stdout), key=lambda p: p["number"])
if a.limit:
    prs = prs[: a.limit]
log(f"{len(prs)} open pull requests")

git("fetch", "-q", a.remote, "main", check=True)
base = git("rev-parse", f"{a.remote}/main", check=True).stdout.strip()
log("base", base)
for i in range(0, len(prs), 100):
    specs = [f"+refs/pull/{p['number']}/head:refs/forge/pr/{p['number']}" for p in prs[i:i + 100]]
    f = git("fetch", "-q", a.remote, *specs)
    if f.returncode:
        log("fetch error", f.stderr.strip()[-300:])

TRAILER = os.environ.get("FORGE_TRAILER", "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
status = {}  # number -> dict(result, detail)
files_of = {}  # number -> files the pull request changes against the base


def ref(n):
    return f"refs/forge/pr/{n}"


def changed(n):
    if n not in files_of:
        files_of[n] = set(git("diff", "--name-only", f"{base}...{ref(n)}").stdout.split())
    return files_of[n]


def reason(h):
    return h if isinstance(h, str) else h.get("reason", "")


def held_now(h, head):
    """A hold naming the pull request's commit (`head`, a prefix) lifts when
    the author pushes another: the new code is tried again. One without a
    commit stays until it is removed from held.json."""
    return isinstance(h, str) or not h.get("head") or head.startswith(h["head"])


todo = []
for p in prs:
    n = p["number"]
    if git("rev-parse", "-q", "--verify", ref(n)).returncode:
        status[n] = {"result": "not fetched"}
    elif p["isDraft"]:
        status[n] = {"result": "draft"}
    elif n in held and held_now(held[n], p["headRefOid"]):
        status[n] = {"result": "held", "detail": reason(held[n])}
    else:
        mt = git("merge-tree", "--write-tree", "--name-only", "--no-messages", base, ref(n))
        if mt.returncode == 1:
            status[n] = {"result": "conflicts with main", "files": mt.stdout.split()[1:6]}
        elif any(f.startswith(".github/workflows/") for f in changed(n)):
            # The Actions token cannot push workflow changes, and the Forge
            # does not run other people's CI changes unreviewed.
            status[n] = {"result": "changes CI workflows",
                         "files": [f for f in changed(n) if f.startswith(".github/workflows/")][:5]}
        elif mt.returncode:
            status[n] = {"result": "error", "detail": mt.stderr.strip()[-200:]}
        else:
            todo.append(p)
log(f"{len(todo)} merge cleanly with main")

git("checkout", "-q", "-B", a.branch, base, check=True)
good = base
merged = []  # numbers in the branch, in order
pending = []


def merge(n, title):
    msg = ["-m", f"Forge: #{n} {title}"] + (["-m", TRAILER] if TRAILER else [])
    r = git("merge", "--no-ff", "-q", *msg, ref(n))
    if r.returncode == 0:
        return None
    files = git("diff", "--name-only", "--diff-filter=U").stdout.split()
    if git("rev-parse", "-q", "--verify", "MERGE_HEAD").returncode == 0:
        git("merge", "--abort")
    else:
        git("reset", "-q", "--hard", "HEAD")
    return files


def settle():
    global good, pending
    if not pending:
        return
    ok, errs = cargo_check()
    if ok:
        merged.extend(n for n, _ in pending)
        for n, _ in pending:
            status[n] = {"result": "in forge"}
        good = git("rev-parse", "HEAD", check=True).stdout.strip()
        log(f"batch of {len(pending)} builds; {len(merged)} in forge")
        pending = []
        return
    log(f"batch of {len(pending)} breaks the build; splitting it")
    batch, pending = pending, []
    git("reset", "-q", "--hard", good, check=True)
    bisect(batch, errs)


def bisect(batch, errs):
    """Adds the pull requests of `batch` that build, halving a failing part
    until the one breaking it is alone (`errs`: the whole batch's errors)."""
    global good
    if len(batch) == 1:
        n, t = batch[0]
        status[n] = {"result": "breaks the build", "detail": errs}
        log(f"#{n} breaks the build: {errs[:1]}")
        return
    half = len(batch) // 2
    for part in (batch[:half], batch[half:]):
        kept = []
        for n, t in part:
            if merge(n, t) is None:
                kept.append((n, t))
            else:
                status[n] = {"result": "conflicts with pull requests", "files": [], "with": []}
        if not kept:
            continue
        ok, part_errs = cargo_check()
        if ok:
            good = git("rev-parse", "HEAD", check=True).stdout.strip()
            merged.extend(n for n, _ in kept)
            for n, _ in kept:
                status[n] = {"result": "in forge"}
        else:
            git("reset", "-q", "--hard", good, check=True)
            bisect(kept, part_errs)


for p in todo:
    n, t = p["number"], p["title"]
    files = merge(n, t)
    if files is None:
        pending.append((n, t))
        if len(pending) >= a.batch:
            settle()
        continue
    # Conflicts here but not with main: with what is already in the branch.
    partners = [m for m in merged + [x for x, _ in pending] if changed(m) & set(files)]
    status[n] = {"result": "conflicts with pull requests", "files": files[:5], "with": partners[:8]}
settle()
git("reset", "-q", "--hard", good, check=True)
log(f"done: {len(merged)} pull requests in {a.branch} at {good}")

# Tests on the final branch.
tests = None
promotion = None
if a.tested_branch:
    subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(os.path.abspath(__file__)), "promotion.py"),
                    "--repo", a.repo, "--out", a.out, "--base", base, "--head", good,
                    "--branch", a.tested_branch, "--test-timeout", str(a.test_timeout),
                    "--diagnostic-runs", str(a.diagnostic_runs),
                    "--diagnostic-seconds", str(a.diagnostic_seconds)], check=True)
    with open(os.path.join(a.out, "promotion.json"), encoding="utf-8") as stream:
        promotion = json.load(stream)
    tests = promotion["candidate"]
    log("tested branch", "promoted" if promotion["promoted"] else "preserved")
elif a.tests:
    import re
    r = subprocess.run(["cargo", "test", "--workspace", "--no-fail-fast"], cwd=a.repo,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=a.test_timeout)
    out = r.stdout + r.stderr
    count = lambda w: sum(int(x) for x in re.findall(rf"(\d+) {w}", out))
    tests = {"passed": count("passed"), "failed": count("failed"), "ignored": count("ignored"),
             "failing": sorted(set(re.findall(r"^test (\S+) \.\.\. FAILED", out, re.M)))}
    log(f"tests: {tests['passed']} passed, {tests['failed']} failed")

previous = {}
if a.previous and os.path.exists(a.previous):
    previous = json.load(open(a.previous, encoding="utf-8")).get("status", {})

# Status page.
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
by = {}
for p in prs:
    s = status.get(p["number"], {"result": "?"})
    by.setdefault(s["result"], []).append((p, s))
order = ["in forge", "conflicts with pull requests", "conflicts with main", "breaks the build",
         "changes CI workflows", "held", "draft", "not fetched", "error", "?"]
json.dump({"generated": now, "base": base, "head": good, "branch": a.branch, "tests": tests,
           "promotion": promotion,
           "status": {p["number"]: status.get(p["number"]) for p in prs}},
          open(os.path.join(a.out, "status.json"), "w", encoding="utf-8"), indent=1)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


md = [f"# VIctory Forge status", "",
      f"Generated {now}. Base: upstream `main` at `{base[:10]}`. Branch `{a.branch}` at `{good[:10]}`: "
      f"**{len(merged)} of {len(prs)} open pull requests** merged, building (`cargo check --workspace --all-targets`) "
      f"and passing the asset policy (`cargo xtask policy`). Rules: [RULES.md](RULES.md).", "",
      "| Result | Pull requests |", "|---|---:|"]
for k in order:
    if k in by:
        md.append(f"| {k} | {len(by[k])} |")
md.append("")
if tests is not None:
    md += ["## Tests on the branch", "",
           f"`cargo test --workspace --no-fail-fast`: **{tests['passed']} passed, {tests['failed']} failed, "
           f"{tests['ignored']} ignored** (on the machine that ran the Forge; GPU tests skip where it has no GPU). "
           "Test failures do not keep a pull request out; they are listed for the authors.", ""]
    md += [f"- `{f}`" for f in tests["failing"]] + [""]
if promotion is not None:
    md += ["## Tested branch", "",
           f"`{cell(promotion['branch'])}`: **{'promoted' if promotion['promoted'] else 'preserved'}**. "
           "Compared with the same upstream commit on the same worker. "
           "This is automated test coverage, not validation of a title or untested GPU paths.", ""]
    baseline = promotion["baseline"]
    md += [f"Baseline: **{baseline['passed']} passed, {baseline['failed']} failed, "
           f"{baseline['ignored']} ignored**. Complete: `{baseline['complete']}`.", ""]
    for label, key in (("Reasons", "reasons"), ("New failures", "new_failures"),
                       ("Previously passing tests no longer passing", "missing_passes")):
        if promotion.get(key):
            md += [f"{label}:", ""] + [f"- {cell(value)}" for value in promotion[key]] + [""]
    diagnosis = promotion.get("diagnosis")
    if diagnosis:
        md += [f"Suspect range: `{diagnosis['last_passing'][:10]}` to "
               f"`{diagnosis['first_failing'][:10]}` after {len(diagnosis['probes'])} probes.", ""]
        md += [f"- `{item['commit'][:10]}` {cell(item['subject'])}" for item in diagnosis["suspects"]]
        md += ["", diagnosis["note"], ""]
if previous:
    was_in = {int(k) for k, v in previous.items() if v and v.get("result") == "in forge"}
    now_in = set(merged)
    gone = sorted(was_in - now_in)
    new = sorted(now_in - was_in)
    md += ["## Since the last run", "",
           f"Joined the branch: {', '.join(f'#{n}' for n in new) or 'none'}.", "",
           f"Left the branch (closed, merged upstream, or now conflicting or failing): "
           f"{', '.join(f'#{n}' for n in gone) or 'none'}.", ""]
for k in order:
    if k not in by:
        continue
    md += [f"## {k} ({len(by[k])})", "", "| PR | Title | Author | Detail |", "|---|---|---|---|"]
    for p, s in by[k]:
        d = ""
        if s.get("files"):
            d = "files: " + ", ".join(f"`{f}`" for f in s["files"])
        if s.get("with"):
            d += "; with " + ", ".join(f"#{m}" for m in s["with"])
        if s.get("detail"):
            d += cell(s["detail"] if isinstance(s["detail"], str) else " / ".join(s["detail"]))
        md.append(f"| [#{p['number']}]({p['url']}) | {cell(p['title'])} | {p['author']['login']} | {cell(d)} |")
    md.append("")
open(os.path.join(a.out, "STATUS.md"), "w", encoding="utf-8").write("\n".join(md))
log("wrote", os.path.join(a.out, "STATUS.md"))

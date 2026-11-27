"""VIctory Forge: upstream main plus every open pull request that merges and builds.

Builds one branch anyone can test, and a status page saying, for each open
pull request, whether it is in that branch, which file it conflicts on (and
with which merged pull requests), or what it breaks.

Usage (from anywhere; needs git >= 2.38, gh, cargo):
    python -I forge.py --repo <VIctory worktree> --out <status folder>
        [--upstream Marvisak/VIctory] [--remote origin] [--branch forge/main]
        [--batch 20] [--held held.json] [--limit N] [--tests] [--previous status.json]
        [--triage-only]

--tests runs `cargo test --workspace --no-fail-fast` on the final branch and
reports it; --previous names the last run's status.json, to list what changed.

The worktree is reset to the forge branch: use a worktree of its own.
Nothing from any game is read or written; only the repository's code.
"""
import argparse, datetime, json, os, subprocess, sys, time

# Isolated mode omits the script's directory from the import path.
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from triage import overlaps, patch_id

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
ap.add_argument("--previous", help="the last run's status.json, to report what changed")
ap.add_argument("--triage-only", action="store_true", help="write a merge and overlap report without building or changing the worktree")
a = ap.parse_args()
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
                    "--json", "number,title,author,isDraft,headRefOid,baseRefName,closingIssuesReferences,url"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode:
    sys.exit(r.stderr)
prs = sorted(json.loads(r.stdout), key=lambda p: p["number"])
if a.limit:
    prs = prs[: a.limit]
log(f"{len(prs)} open pull requests")

git("fetch", "-q", a.remote, "main", check=True)
base = git("rev-parse", f"{a.remote}/main", check=True).stdout.strip()
base_tree = git("rev-parse", f"{base}^{{tree}}", check=True).stdout.strip()
log("base", base)


def ref(n):
    return f"refs/forge/pr/{n}"


def fetched_heads():
    refs = git("for-each-ref", "--format=%(refname) %(objectname)", "refs/forge/pr/", check=True).stdout
    return dict(line.split() for line in refs.splitlines())


heads = fetched_heads()
need_fetch = [p for p in prs if heads.get(ref(p["number"])) != p["headRefOid"]]
log(f"fetching {len(need_fetch)} PR heads, reusing {len(prs) - len(need_fetch)} pinned heads")
for i in range(0, len(need_fetch), 100):
    specs = [f"+refs/pull/{p['number']}/head:{ref(p['number'])}" for p in need_fetch[i:i + 100]]
    f = git("fetch", "-q", a.remote, *specs)
    if f.returncode:
        log("fetch error", f.stderr.strip()[-300:])
if need_fetch:
    heads = fetched_heads()

TRAILER = os.environ.get("FORGE_TRAILER", "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
status = {}  # number -> dict(result, detail)
files_of = {}  # number -> files the pull request changes against the base


def changed(n):
    if n not in files_of:
        paths = git("diff", "--name-only", "-z", f"{base}...{heads[ref(n)]}", check=True).stdout
        files_of[n] = set(paths.strip("\0").split("\0")) if paths else set()
    return files_of[n]


def reason(h):
    return h if isinstance(h, str) else h.get("reason", "")


def held_now(h, head):
    """A hold naming the pull request's commit (`head`, a prefix) lifts when
    the author pushes another: the new code is tried again. One without a
    commit stays until it is removed from held.json."""
    return isinstance(h, str) or not h.get("head") or head.startswith(h["head"])


todo = []
participants = []
fingerprints = {}
for p in prs:
    n = p["number"]
    fetched = heads.get(ref(n))
    if not fetched:
        status[n] = {"result": "not fetched"}
    elif fetched != p["headRefOid"]:
        status[n] = {"result": "head changed"}
    elif p["isDraft"]:
        status[n] = {"result": "draft"}
    elif p["baseRefName"] != "main":
        status[n] = {"result": "alternate base", "detail": p["baseRefName"]}
    elif n in held and held_now(held[n], p["headRefOid"]):
        status[n] = {"result": "held", "detail": reason(held[n])}
    else:
        mt = git("merge-tree", "--write-tree", "--name-only", "--no-messages", "-z", base, fetched)
        tree, *paths = mt.stdout.strip("\0").split("\0")
        if mt.returncode in (0, 1):
            changed(n)
            participants.append(p)
        if mt.returncode == 1:
            status[n] = {"result": "conflicts with main", "files": paths, "against": base}
        elif mt.returncode:
            status[n] = {"result": "error", "detail": mt.stderr.strip()[-200:]}
        elif tree == base_tree:
            status[n] = {"result": "already in main"}
        elif any(f.startswith(".github/workflows/") for f in changed(n)):
            # The Actions token cannot push workflow changes, and the Forge
            # does not run other people's CI changes unreviewed.
            status[n] = {"result": "changes CI workflows",
                         "files": [f for f in changed(n) if f.startswith(".github/workflows/")][:5]}
        else:
            fingerprint = patch_id(a.repo, base, fetched)
            if fingerprint:
                fingerprints[n] = (fingerprint, tree)
            todo.append(p)
log(f"{len(todo)} merge cleanly with main")
duplicates = overlaps(participants, files_of, fingerprints)

if not a.triage_only:
    git("checkout", "-q", "-B", a.branch, base, check=True)
good = base
merged = []  # numbers in the branch, in order
pending = []


def merge(n, title):
    msg = ["-m", f"Forge: #{n} {title}"] + (["-m", TRAILER] if TRAILER else [])
    r = git("merge", "--no-ff", "-q", *msg, heads[ref(n)])
    if r.returncode == 0:
        return None
    paths = git("diff", "--name-only", "--diff-filter=U", "-z").stdout
    files = paths.strip("\0").split("\0") if paths else []
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
            files = merge(n, t)
            if files is None:
                kept.append((n, t))
            else:
                status[n] = {"result": "conflicts with pull requests", "files": files,
                             "with": [m for m in merged + [x for x, _ in kept] if changed(m) & set(files)][:8],
                             "against": git("rev-parse", "HEAD", check=True).stdout.strip()}
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
    if a.triage_only:
        status[n] = {"result": "clean preview"}
        continue
    files = merge(n, t)
    if files is None:
        pending.append((n, t))
        if len(pending) >= a.batch:
            settle()
        continue
    # Conflicts here but not with main: with what is already in the branch.
    partners = [m for m in merged + [x for x, _ in pending] if changed(m) & set(files)]
    status[n] = {"result": "conflicts with pull requests", "files": files, "with": partners[:8],
                 "against": git("rev-parse", "HEAD", check=True).stdout.strip()}
settle()
if not a.triage_only:
    git("reset", "-q", "--hard", good, check=True)
    log(f"done: {len(merged)} pull requests in {a.branch} at {good}")

# Tests on the final branch.
tests = None
if a.tests and not a.triage_only:
    import re
    r = subprocess.run(["cargo", "test", "--workspace", "--no-fail-fast"], cwd=a.repo,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=7200)
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
    s = status.setdefault(p["number"], {"result": "?"})
    s["head"] = p["headRefOid"]
    by.setdefault(s["result"], []).append((p, s))
order = ["in forge", "clean preview", "already in main", "conflicts with pull requests", "conflicts with main",
         "breaks the build", "changes CI workflows", "held", "draft", "alternate base", "not fetched",
         "head changed", "error", "?"]
json.dump({"generated": now, "base": base, "head": good, "branch": a.branch, "tests": tests,
           "triage_only": a.triage_only, "overlaps": duplicates, "status": status},
          open(os.path.join(a.out, "status.json"), "w", encoding="utf-8"), indent=1)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


md = ["# VIctory Forge status", "",
      f"Generated {now}. Base: upstream `main` at `{base[:10]}`. Branch `{a.branch}` at `{good[:10]}`: "
      f"**{len(merged)} of {len(prs)} open pull requests** merged, building (`cargo check --workspace --all-targets`) "
      f"and passing the asset policy (`cargo xtask policy`). Rules: [RULES.md](RULES.md).", "",
      "| Result | Pull requests |", "|---|---:|"]
if a.triage_only:
    md[2] = f"Generated {now}. Merge previews for {len(prs)} open PRs against `main` at `{base[:10]}`."
for k in order:
    if k in by:
        md.append(f"| {k} | {len(by[k])} |")
md.append("")
if duplicates:
    md += [f"## Potential overlaps ({len(duplicates)})", "",
           "Review these pairs before labeling a duplicate. Both branches may have useful tests.", "",
           "| Pull requests | Evidence |", "|---|---|"]
    urls = {p["number"]: p["url"] for p in prs}
    for pair in duplicates:
        links = " / ".join(f"[#{n}]({urls[n]})" for n in pair["prs"])
        evidence = pair["reason"]
        if pair.get("issues"):
            evidence += " " + ", ".join(f"#{n}" for n in pair["issues"])
        if pair.get("files"):
            evidence += " in " + ", ".join(f"`{path}`" for path in pair["files"][:3])
        md.append(f"| {links} | {cell(evidence)} |")
    md.append("")
if tests is not None:
    md += ["## Tests on the branch", "",
           f"`cargo test --workspace --no-fail-fast`: **{tests['passed']} passed, {tests['failed']} failed, "
           f"{tests['ignored']} ignored** (on the machine that ran the Forge; GPU tests skip where it has no GPU). "
           "Test failures do not keep a pull request out; they are listed for the authors.", ""]
    md += [f"- `{f}`" for f in tests["failing"]] + [""]
if previous and not a.triage_only:
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
            d = "files: " + ", ".join(f"`{f}`" for f in s["files"][:5])
        if s.get("against"):
            d += f"; merge target `{s['against'][:10]}`"
        if s.get("with"):
            d += "; with " + ", ".join(f"#{m}" for m in s["with"])
        if s.get("detail"):
            d += cell(s["detail"] if isinstance(s["detail"], str) else " / ".join(s["detail"]))
        author = (p.get("author") or {}).get("login", "")
        md.append(f"| [#{p['number']}]({p['url']}) | {cell(p['title'])} | {author} | {cell(d)} |")
    md.append("")
open(os.path.join(a.out, "STATUS.md"), "w", encoding="utf-8").write("\n".join(md))
log("wrote", os.path.join(a.out, "STATUS.md"))

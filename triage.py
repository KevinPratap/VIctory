"""Read Forge triage results, prepare merges, and close confirmed duplicates."""

import argparse
from collections import defaultdict
import itertools
import json
from pathlib import Path
import re
import subprocess


def patch_id(repo, base, head):
    diff = subprocess.run(
        ["git", "diff", "--no-ext-diff", "--no-textconv", "--no-color", "--binary", f"{base}...{head}"],
        cwd=repo, capture_output=True, check=True,
    )
    ids = subprocess.run(["git", "patch-id", "--stable"], input=diff.stdout,
                         capture_output=True, check=True).stdout.split()
    return ids[0].decode("ascii") if ids else None


def overlaps(prs, files, fingerprints):
    """Return pairs with the same merge result or a shared issue/title and files."""
    exact = defaultdict(list)
    for n, key in fingerprints.items():
        exact[key].append(n)
    strong = {tuple(sorted(pair)) for group in exact.values() for pair in itertools.combinations(group, 2)}

    stop_words = {"fix", "the", "and", "for", "with", "from", "when", "gpu", "shader", "shaders", "hle"}
    titles, issues = {}, {}
    for p in prs:
        n = p["number"]
        titles[n] = set(re.findall(r"[a-z][a-z_0-9]{2,}", p["title"].lower())) - stop_words
        issues[n] = {i["number"] for i in p.get("closingIssuesReferences", [])}

    pairs = []
    for a, b in itertools.combinations(sorted(titles), 2):
        if (a, b) in strong:
            pairs.append({"prs": [a, b], "reason": "same patch ID and merge tree"})
            continue
        common = files[a] & files[b]
        if not common:
            continue
        shared = issues[a] & issues[b]
        similar = len(titles[a] & titles[b]) / max(1, len(titles[a] | titles[b]))
        if shared or similar >= 0.70:
            pairs.append({"prs": [a, b], "reason": "shared issue" if shared else "similar title",
                          "issues": sorted(shared), "files": sorted(common)})
    return pairs


def git(repo, *args, check=True):
    return subprocess.run(["git", "-C", str(repo), *args], check=check,
                          capture_output=True, text=True, encoding="utf-8")


def full_commit(repo, sha):
    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ValueError("Expected a full commit SHA from the Forge report.")
    if git(repo, "cat-file", "-e", f"{sha}^{{commit}}", check=False).returncode:
        raise ValueError(f"Fetch commit {sha} into {repo} first, then rerun this command.")
    return sha


def prepare_merge(repo, worktree, status, number):
    """Merge the reported target into a detached worktree at the reported PR head."""
    entry = status["status"].get(str(number)) or {}
    if entry.get("result") not in {"conflicts with main", "conflicts with pull requests"}:
        raise ValueError(f"PR #{number} has no conflict in this report.")
    head = full_commit(repo, entry.get("head"))
    against = full_commit(repo, entry.get("against"))
    dest = Path(worktree).resolve()
    if dest.exists():
        raise ValueError(f"Choose a new worktree path. {dest} already exists.")
    git(repo, "worktree", "add", "--detach", str(dest), head)
    merge = git(dest, "-c", "rerere.enabled=true", "-c", "rerere.autoupdate=true",
                "merge", "--no-commit", "--no-ff", against, check=False)
    if git(dest, "rev-parse", "-q", "--verify", "MERGE_HEAD", check=False).returncode and merge.returncode:
        raise RuntimeError(f"Merge failed in {dest}: {merge.stderr.strip()}")
    pending = git(dest, "diff", "--name-only", "--diff-filter=U", "-z").stdout.strip("\0")
    return dest, pending.split("\0") if pending else [], merge.stderr.strip()


def github(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True, encoding="utf-8").stdout


def close_duplicate(repo, duplicate, canonical, head, apply=False):
    """Apply an explicit maintainer decision. Inferred matches never call this."""
    if duplicate == canonical or min(duplicate, canonical) < 1:
        raise ValueError("Choose two different pull requests.")
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise ValueError("Supply the full reviewed head SHA.")

    def view(number):
        return json.loads(github("pr", "view", str(number), "-R", repo, "--json",
                                 "state,headRefOid,labels,baseRefName,isDraft"))

    target = view(canonical)
    if target["state"] not in {"OPEN", "MERGED"} or target["isDraft"]:
        raise ValueError("The canonical PR must be open and ready for review, or merged.")
    if apply:
        permissions = json.loads(github("api", f"repos/{repo}")).get("permissions", {})
        if not any(permissions.get(key) for key in ("push", "maintain", "admin")):
            raise ValueError("Closing requires a maintainer account with write access to the upstream repository.")
    candidate = view(duplicate)
    if candidate["state"] != "OPEN" or candidate["headRefOid"] != head:
        raise ValueError("The duplicate must still be open at its reviewed head.")
    if candidate["baseRefName"] != target["baseRefName"]:
        raise ValueError("Both pull requests must target the same branch.")
    if "duplicate" not in {label["name"] for label in candidate["labels"]}:
        raise ValueError("A maintainer must apply the duplicate label first.")
    if apply:
        github("pr", "close", str(duplicate), "-R", repo, "--comment",
               f"Duplicate of #{canonical}. Please continue review there.")
    return f"{'Closed' if apply else 'Would close'} #{duplicate} as a duplicate of #{canonical}."


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    resolve = sub.add_parser("resolve", help="prepare a separate worktree and reuse recorded Git resolutions")
    resolve.add_argument("--repo", required=True)
    resolve.add_argument("--status", type=Path, required=True)
    resolve.add_argument("--pr", type=int, required=True)
    resolve.add_argument("--worktree", required=True)
    close = sub.add_parser("close", help="close an explicitly reviewed and labeled duplicate")
    close.add_argument("--upstream", default="Marvisak/VIctory")
    close.add_argument("--pr", type=int, required=True)
    close.add_argument("--canonical", type=int, required=True)
    close.add_argument("--head", required=True)
    close.add_argument("--apply", action="store_true", help="close the PR instead of previewing the decision")
    a = ap.parse_args()
    try:
        if a.command == "close":
            print(close_duplicate(a.upstream, a.pr, a.canonical, a.head, a.apply))
            return 0
        status = json.loads(a.status.read_text(encoding="utf-8"))
        dest, pending, messages = prepare_merge(a.repo, a.worktree, status, a.pr)
    except (ValueError, OSError, RuntimeError, subprocess.CalledProcessError) as e:
        ap.exit(2, f"{getattr(e, 'stderr', None) or e}\n")
    print(f"Merge worktree: {dest}")
    if messages:
        print(messages)
    if pending:
        print("Files still needing a resolution:")
        for path in pending:
            print(f"  {path}")
        return 1
    print("Review the staged changes, run the checks, then commit in the worktree if appropriate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Compare Forge tests with a pinned baseline and conditionally advance a ref.

No pull requests are fetched and no branches are published. Cargo may download
dependencies. Use a clean, disposable worktree; the original checkout is restored
and an existing tested ref survives rejection.
"""
import argparse
import json
import os
import re
import signal
import subprocess
import time


def parse_tests(output, returncode, timed_out=False):
    """Read ordinary Cargo/libtest output; refuse incomplete or ambiguous runs."""
    target = None
    outcomes = {}
    summaries = []
    problems = []
    targets_started = 0
    targets_finished = 0
    target_summaries = 0
    for line in output.splitlines():
        line = re.sub(r"\x1b\[[0-9;]*m", "", line).strip()
        running = re.match(r"Running (.+) \((.+)\)$", line)
        if running or line.startswith("Doc-tests "):
            if target is not None and target_summaries:
                targets_finished += 1
            targets_started += 1
            target_summaries = 0
        if running:
            binary = running[2].replace("\\", "/").rsplit("/", 1)[-1]
            binary = re.sub(r"-[0-9a-f]{7,}(?:\.exe)?$", "", binary)
            target = f"{running[1].replace(chr(92), '/')} [{binary}]"
        elif line.startswith("Doc-tests "):
            target = line
        result = re.match(r"test (.+) \.\.\. (ok|FAILED|ignored(?:,.*)?)$", line)
        if result:
            key = f"{target}::{result[1]}"
            if target is None or key in outcomes:
                problems.append("unidentified or duplicate test result")
            outcomes[key] = "ignored" if result[2].startswith("ignored") else result[2]
        summary = re.match(
            r"test result: (?:ok|FAILED)\. (\d+) passed; (\d+) failed; (\d+) ignored;", line)
        if summary:
            summaries.append(tuple(map(int, summary.groups())))
            target_summaries += 1
            if target is None:
                problems.append("test summary without an identified target")
        if line.startswith("error:") and not re.match(
                r"error: (?:test failed,|doctest failed,|\d+ targets? failed:)", line):
            problems.append(line[:300])
    counts = [sum(s[i] for s in summaries) for i in range(3)]
    if target is not None and target_summaries:
        targets_finished += 1
    if targets_started != targets_finished:
        problems.append("a test target did not finish")
    observed = [sum(v == state for v in outcomes.values()) for state in ("ok", "FAILED", "ignored")]
    if not summaries or counts != observed:
        problems.append("test summaries and named outcomes are incomplete")
    if not counts[0]:
        problems.append("no passing tests were observed")
    if returncode not in (0, 101) or (returncode == 101 and not counts[1]):
        problems.append(f"test command exited {returncode}")
    if returncode == 0 and counts[1]:
        problems.append("test failures with a successful exit code")
    if timed_out:
        problems.append("test command timed out")
    return {"passed": counts[0], "failed": counts[1], "ignored": counts[2],
            "failing": sorted(k for k, v in outcomes.items() if v == "FAILED"),
            "passing": sorted(k for k, v in outcomes.items() if v == "ok"),
            "complete": not problems, "problems": sorted(set(problems)),
            "returncode": returncode, "timed_out": timed_out}


def verdict(baseline, candidate):
    new = sorted(set(candidate["failing"]) - set(baseline["failing"]))
    missing = sorted(set(baseline["passing"]) - set(candidate["passing"]))
    reasons = []
    if not baseline["complete"]:
        reasons.append("baseline test run is incomplete")
    if not candidate["complete"]:
        reasons.append("candidate test run is incomplete")
    if new:
        reasons.append("new test failures")
    if missing:
        reasons.append("previously passing tests no longer pass or were not run")
    return {"eligible": not reasons, "reasons": reasons,
            "new_failures": new, "missing_passes": missing}


def investigate(history, base, baseline, candidate, probe, max_runs):
    """Bound a regression along merge prefixes, without asserting causality.

    Earlier changes may interact with changes in the suspect range. Nonmonotonic
    failures and flakes require manual confirmation; untestable prefixes stop
    the search rather than being misclassified as regressions.
    """
    low, high = 0, len(history)
    probes = []
    candidate_check = verdict(baseline, candidate)
    target_failures = set(candidate_check["new_failures"])
    target_missing = set(candidate_check["missing_passes"])
    for _ in range(max_runs):
        if high - low <= 1:
            break
        mid = (low + high) // 2
        result = probe(history[mid - 1]["commit"])
        if result is None:
            break
        check = verdict(baseline, result)
        probes.append({"prefix": mid, "commit": history[mid - 1]["commit"],
                       "complete": result["complete"], "new_failures": check["new_failures"],
                       "missing_passes": check["missing_passes"]})
        if not result["complete"]:
            break
        if check["eligible"]:
            low = mid
        elif target_failures.intersection(check["new_failures"]) or target_missing.intersection(check["missing_passes"]):
            high = mid
        else:
            # A transient failure in a different test does not locate the
            # candidate's regression. Leave the wider range unresolved.
            probes[-1]["inconclusive"] = "different regression from the candidate"
            break
    return {"last_passing": base if not low else history[low - 1]["commit"],
            "first_failing": history[high - 1]["commit"],
            "suspects": history[low:high], "probes": probes,
            "narrowed_to_one_merge": high - low == 1,
            "target_failures": sorted(target_failures),
            "note": "Suspect range only: earlier PRs may interact with it; flakes and "
                    "nonmonotonic failures need confirmation. No PR is automatically held."}


def run_tests(repo, log_path, timeout, command=None):
    started = time.monotonic()
    timed_out = False
    env = os.environ.copy()
    env["CARGO_TERM_COLOR"] = "never"
    for key in ("GH_TOKEN", "GITHUB_TOKEN"):
        env.pop(key, None)
    command = command or ["cargo", "test", "--workspace", "--no-fail-fast", "--locked", "--color", "never"]
    group = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
    with open(log_path, "w", encoding="utf-8") as stream:
        try:
            process = subprocess.Popen(command, cwd=repo, stdout=stream, stderr=subprocess.STDOUT,
                                       env=env, **group)
            try:
                code = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                code = -1
            finally:
                # Cargo owns compiler/test children. Stop the entire group so a
                # timeout or interrupt cannot mutate the next prefix's files.
                if process.poll() is None:
                    try:
                        if os.name == "nt":
                            subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                                           capture_output=True, timeout=10)
                        else:
                            try:
                                os.killpg(process.pid, signal.SIGKILL)
                            except ProcessLookupError:
                                pass
                    finally:
                        process.kill()
                        process.wait(timeout=10)
        except (OSError, subprocess.TimeoutExpired) as error:
            stream.write(str(error))
            code = -1
    with open(log_path, encoding="utf-8", errors="replace") as stream:
        output = stream.read()
    result = parse_tests(output, code, timed_out)
    result.update(seconds=round(time.monotonic() - started, 3), log=os.path.basename(log_path))
    return result


def promote(repo, out, base, head, branch="forge/tested", test_timeout=1800,
            diagnostic_runs=6, diagnostic_seconds=900, runner=run_tests):
    repo, out = os.path.abspath(repo), os.path.abspath(out)
    os.makedirs(out, exist_ok=True)

    def git(*args, check=True):
        result = subprocess.run(["git", *args], cwd=repo, capture_output=True,
                                text=True, encoding="utf-8", errors="replace")
        if check and result.returncode:
            raise RuntimeError(f"git {' '.join(args)}: {result.stderr.strip()}")
        return result.stdout.strip()

    def clean():
        if git("status", "--porcelain", "--untracked-files=normal"):
            raise RuntimeError("worktree has changes; nothing will be discarded")

    report = {"branch": branch, "promoted": False, "base": base, "head": head,
              "baseline": None, "candidate": None, "diagnosis": None}
    original_branch = original_head = None
    moved = False
    try:
        clean()
        git("check-ref-format", "--branch", branch)
        original_branch = git("symbolic-ref", "--quiet", "--short", "HEAD", check=False)
        original_head = git("rev-parse", "HEAD")
        if f"branch refs/heads/{branch}" in git("worktree", "list", "--porcelain").splitlines():
            raise RuntimeError("tested branch is checked out in a worktree")
        base = git("rev-parse", "--verify", "--end-of-options", base + "^{commit}")
        head = git("rev-parse", "--verify", "--end-of-options", head + "^{commit}")
        if original_head != head:
            raise RuntimeError("worktree must start at the candidate head")
        git("merge-base", "--is-ancestor", base, head)
        previous = git("rev-parse", "--verify", f"refs/heads/{branch}", check=False)
        report.update(base=base, head=head, previous_head=previous or None)

        def run(commit, label, timeout):
            nonlocal moved
            clean()
            git("checkout", "--quiet", "--detach", commit)
            moved = True
            print(f"Testing {label} at {commit[:10]} (timeout {timeout:.0f}s)", flush=True)
            result = runner(repo, os.path.join(out, label + ".log"), timeout)
            clean()
            result["commit"] = commit
            return result

        baseline = report["baseline"] = run(base, "baseline", test_timeout)
        candidate = report["candidate"] = run(head, "candidate", test_timeout)
        report.update(verdict(baseline, candidate))
        if (not report["eligible"] and baseline["complete"] and candidate["complete"]
                and diagnostic_runs and diagnostic_seconds):
            deadline = time.monotonic() + diagnostic_seconds
            lines = git("log", "--first-parent", "--reverse", "--format=%H%x09%s", f"{base}..{head}").splitlines()
            history = [{"commit": line.split("\t", 1)[0], "subject": line.split("\t", 1)[1]}
                       for line in lines]
            if history and git("rev-parse", history[0]["commit"] + "^1") == base:
                counter = 0

                def probe(commit):
                    nonlocal counter
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        return None
                    counter += 1
                    return run(commit, f"probe-{counter:02d}", min(test_timeout, remaining))

                report["diagnosis"] = investigate(
                    history, base, baseline, candidate, probe, diagnostic_runs)
    except (RuntimeError, OSError) as error:
        report["error"] = str(error)
    finally:
        if moved:
            try:
                clean()
                if original_branch and git("rev-parse", original_branch) != original_head:
                    raise RuntimeError("original branch changed during testing")
                git("checkout", "--quiet", original_branch or "--detach",
                    *([] if original_branch else [original_head]))
                if git("rev-parse", "HEAD") != original_head:
                    raise RuntimeError("original checkout could not be verified")
            except (RuntimeError, OSError) as error:
                report["restore_error"] = str(error)
    if report.get("eligible") and not report.get("error") and not report.get("restore_error"):
        try:
            clean()
            git("update-ref", f"refs/heads/{branch}", head, previous or "0" * len(head))
            report["promoted"] = True
        except (RuntimeError, OSError) as error:
            report["error"] = str(error)
    with open(os.path.join(out, "promotion.json"), "w", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--branch", default="forge/tested")
    parser.add_argument("--test-timeout", type=int, default=1800)
    parser.add_argument("--diagnostic-runs", type=int, default=6)
    parser.add_argument("--diagnostic-seconds", type=int, default=900)
    args = parser.parse_args()
    if args.test_timeout <= 0 or args.diagnostic_runs < 0 or args.diagnostic_seconds < 0:
        parser.error("timeouts must be positive and diagnostic budgets nonnegative")
    report = promote(**vars(args))
    print("Tested branch:", "promoted" if report["promoted"] else "preserved", flush=True)
    return int(bool(report.get("error") or report.get("restore_error")))


if __name__ == "__main__":
    raise SystemExit(main())

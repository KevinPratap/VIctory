"""Source-only regression tests: no Cargo, network, GPU or game data required."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("promotion", Path(__file__).with_name("promotion.py"))
promotion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(promotion)


def output(passing=("healthy",), failing=(), ignored=(), binary="suite", label="unittests src/lib.rs"):
    lines = [f"Running {label} (target/debug/deps/{binary}-0123456789abcdef.exe)"]
    lines += [f"test {name} ... ok" for name in passing]
    lines += [f"test {name} ... FAILED" for name in failing]
    lines += [f"test {name} ... ignored" for name in ignored]
    lines += [f"test result: {'FAILED' if failing else 'ok'}. {len(passing)} passed; "
              f"{len(failing)} failed; {len(ignored)} ignored; 0 measured; 0 filtered out; finished in 0.01s"]
    if failing:
        lines += ["error: test failed, to rerun pass `--lib`"]
    return "\n".join(lines) + "\n"


def result(passing=("healthy",), failing=(), ignored=(), binary="suite"):
    return promotion.parse_tests(output(passing, failing, ignored, binary), 101 if failing else 0)


class ParsingTests(unittest.TestCase):
    def test_baseline_failure_is_allowed_but_new_failure_is_not(self):
        baseline = result(failing=("known",))
        self.assertTrue(promotion.verdict(baseline, result(failing=("known",)))["eligible"])
        self.assertTrue(promotion.verdict(baseline, result())["eligible"])
        check = promotion.verdict(baseline, result(failing=("known", "new")))
        self.assertFalse(check["eligible"])
        self.assertEqual(len(check["new_failures"]), 1)

    def test_same_name_in_different_targets_cannot_hide_a_regression(self):
        text = output(failing=("collision",), binary="first") + output(binary="second")
        baseline = promotion.parse_tests(text, 101)
        text = output(binary="first") + output(failing=("collision",), binary="second")
        candidate = promotion.parse_tests(text, 101)
        self.assertTrue(baseline["complete"])
        self.assertTrue(candidate["complete"])
        self.assertFalse(promotion.verdict(baseline, candidate)["eligible"])

    def test_removed_or_ignored_passing_tests_block_promotion(self):
        baseline = result(passing=("healthy", "important"))
        for candidate in (result(), result(ignored=("important",))):
            with self.subTest(candidate=candidate):
                self.assertTrue(promotion.verdict(baseline, candidate)["missing_passes"])

    def test_compile_crash_timeout_and_empty_runs_fail_closed(self):
        cases = [("error: could not compile `broken`", 101, False),
                 (output(), 1, False), (output(), 0, True), ("", 0, False),
                 (output() + "error: could not compile `later`", 101, False),
                 (output(passing=(), failing=("broken",)), 101, False)]
        for text, code, timeout in cases:
            with self.subTest(text=text, code=code):
                self.assertFalse(promotion.parse_tests(text, code, timeout)["complete"])

    def test_incomplete_or_unidentified_outcomes_are_not_success(self):
        text = output().replace("test healthy ... ok\n", "")
        self.assertFalse(promotion.parse_tests(text, 0)["complete"])
        self.assertFalse(promotion.parse_tests("\n".join(output().splitlines()[1:]), 0)["complete"])

    def test_crashed_target_cannot_hide_behind_another_known_failure(self):
        text = output(failing=("known",)) + "Running unittests src/lib.rs (target/debug/deps/crashed-0123456789abcdef.exe)\n"
        text += "error: test failed, to rerun pass `-p crashed --lib`\n"
        self.assertFalse(promotion.parse_tests(text, 101)["complete"])

    def test_doctests_and_windows_paths_are_qualified(self):
        text = output().replace("target/debug/deps/", "target\\debug\\deps\\")
        text += ("Doc-tests docs\ntest src/lib.rs - example (line 4) ... ok\n"
                 "test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s\n")
        parsed = promotion.parse_tests(text, 0)
        self.assertTrue(parsed["complete"])
        self.assertEqual(parsed["passed"], 2)
        self.assertTrue(any(key.startswith("Doc-tests docs::") for key in parsed["passing"]))


class InvestigationTests(unittest.TestCase):
    def test_interacting_changes_are_reported_as_a_range_not_a_proven_culprit(self):
        history = [{"commit": str(n), "subject": f"Forge: #{n}"} for n in range(1, 9)]
        calls = []

        def probe(commit):
            calls.append(commit)
            return result(failing=("interaction",)) if int(commit) >= 6 else result()

        report = promotion.investigate(history, "base", result(), result(failing=("interaction",)), probe, 6)
        self.assertEqual([item["commit"] for item in report["suspects"]], ["6"])
        self.assertEqual(report["last_passing"], "5")
        self.assertLessEqual(len(calls), 6)
        self.assertIn("earlier PRs may interact", report["note"])

    def test_budget_and_untestable_prefix_keep_the_unresolved_range(self):
        history = [{"commit": str(n), "subject": "merge"} for n in range(1, 17)]
        bad = result(failing=("new",))
        for probe, budget in ((lambda _: result(), 1),
                              (lambda _: promotion.parse_tests("compile error", 101), 6),
                              (lambda _: None, 6)):
            report = promotion.investigate(history, "base", result(), bad, probe, budget)
            self.assertFalse(report["narrowed_to_one_merge"])
            self.assertLessEqual(len(report["probes"]), budget)

    def test_unrelated_prefix_failure_does_not_get_blamed_for_candidate_failure(self):
        history = [{"commit": str(n), "subject": "merge"} for n in range(1, 9)]
        report = promotion.investigate(history, "base", result(), result(failing=("candidate_failure",)),
                                       lambda _: result(failing=("unrelated_failure",)), 6)
        self.assertEqual(len(report["suspects"]), len(history))
        self.assertEqual(report["probes"][0]["inconclusive"], "different regression from the candidate")


class CommandTests(unittest.TestCase):
    def test_real_process_output_is_parsed_and_credentials_are_not_inherited(self):
        with tempfile.TemporaryDirectory(prefix="forge-command-") as directory:
            command = [sys.executable, "-I", "-c", "import os,sys; "
                       "sys.exit(2) if any(k in os.environ for k in ('GH_TOKEN','GITHUB_TOKEN')) else None; "
                       f"print({output()!r})"]
            with mock.patch.dict(os.environ, {"GH_TOKEN": "test-sentinel", "GITHUB_TOKEN": "test-sentinel"}):
                parsed = promotion.run_tests(directory, os.path.join(directory, "test.log"), 10, command)
            self.assertTrue(parsed["complete"])

    def test_timeout_stops_a_real_process_and_returns_an_incomplete_result(self):
        with tempfile.TemporaryDirectory(prefix="forge-timeout-") as directory:
            started = time.monotonic()
            command = [sys.executable, "-I", "-c", "import time; time.sleep(60)"]
            parsed = promotion.run_tests(directory, os.path.join(directory, "test.log"), 0.2, command)
            self.assertTrue(parsed["timed_out"])
            self.assertFalse(parsed["complete"])
            self.assertLess(time.monotonic() - started, 10)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="forge-test-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        self.out = Path(self.temp.name) / "out"
        self.git("init", "-q", "-b", "candidate")
        self.git("config", "user.name", "Forge test")
        self.git("config", "user.email", "forge-test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.autocrlf", "false")
        (self.repo / "source.txt").write_text("base\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "baseline")
        self.base = self.git("rev-parse", "HEAD")
        self.git("branch", "forge/tested", self.base)
        self.git("switch", "-q", "-c", "change")
        (self.repo / "source.txt").write_text("candidate\n", encoding="utf-8")
        self.git("commit", "-q", "-am", "change")
        self.git("switch", "-q", "candidate")
        self.git("merge", "-q", "--no-ff", "change", "-m", "Forge: #1 test change")
        self.head = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, capture_output=True,
                              text=True, check=True).stdout.strip()

    def run_promotion(self, candidate=None, baseline=None, **kwargs):
        def runner(repo, log_path, timeout):
            current = self.git("rev-parse", "HEAD")
            parsed = baseline if current == self.base else candidate
            Path(log_path).write_text("synthetic test log\n", encoding="utf-8")
            return dict(parsed if parsed is not None else result())

        return promotion.promote(str(self.repo), str(self.out), self.base, self.head,
                                 runner=runner, **kwargs)

    def test_success_advances_tested_and_restores_candidate(self):
        report = self.run_promotion()
        self.assertTrue(report["promoted"])
        self.assertEqual(self.git("rev-parse", "forge/tested"), self.head)
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), "candidate")
        self.assertEqual(self.git("rev-parse", "HEAD"), self.head)
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertTrue(json.loads((self.out / "promotion.json").read_text())["promoted"])

    def test_rejection_preserves_last_tested_and_restores_candidate(self):
        report = self.run_promotion(candidate=result(failing=("new",)))
        self.assertFalse(report["promoted"])
        self.assertEqual(self.git("rev-parse", "forge/tested"), self.base)
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), "candidate")
        self.assertTrue(report["diagnosis"]["narrowed_to_one_merge"])

    def test_incomplete_baseline_blocks_an_otherwise_passing_candidate(self):
        report = self.run_promotion(baseline=promotion.parse_tests("build failed", 101))
        self.assertFalse(report["promoted"])
        self.assertEqual(self.git("rev-parse", "forge/tested"), self.base)
        self.assertIsNone(report["diagnosis"])

    def test_dirty_worktree_is_preserved(self):
        (self.repo / "source.txt").write_text("user work\n", encoding="utf-8")
        report = self.run_promotion()
        self.assertFalse(report["promoted"])
        self.assertIn("nothing will be discarded", report["error"])
        self.assertEqual((self.repo / "source.txt").read_text(), "user work\n")

    def test_checked_out_tested_branch_is_protected(self):
        self.git("switch", "-q", "forge/tested")
        report = promotion.promote(str(self.repo), str(self.out), self.base, self.base)
        self.assertFalse(report["promoted"])
        self.assertIn("checked out", report["error"])
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), "forge/tested")

    def test_concurrent_tested_ref_update_is_not_overwritten(self):
        def runner(repo, log_path, timeout):
            self.git("update-ref", "refs/heads/forge/tested", self.head)
            return result()

        report = promotion.promote(str(self.repo), str(self.out), self.base, self.head, runner=runner)
        self.assertFalse(report["promoted"])
        self.assertIn("update-ref", report["error"])
        self.assertEqual(self.git("rev-parse", "forge/tested"), self.head)
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), "candidate")

    def test_test_generated_changes_are_preserved_and_block_promotion(self):
        def runner(repo, log_path, timeout):
            (self.repo / "source.txt").write_text("test generated change\n", encoding="utf-8")
            return result()

        report = promotion.promote(str(self.repo), str(self.out), self.base, self.head, runner=runner)
        self.assertFalse(report["promoted"])
        self.assertIn("restore_error", report)
        self.assertEqual(self.git("rev-parse", "forge/tested"), self.base)
        self.assertEqual((self.repo / "source.txt").read_text(), "test generated change\n")


if __name__ == "__main__":
    unittest.main()

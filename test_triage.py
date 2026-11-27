import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from triage import close_duplicate, git, overlaps, patch_id, prepare_merge


class TriageTests(unittest.TestCase):
    def test_likely_overlaps_require_shared_code(self):
        prs = [{"number": n, "title": title, "closingIssuesReferences": [{"number": 60}]}
               for n, title in [(1, "Shader branch condition"), (2, "Test branch flags"),
                                (3, "GPU allocator guard"), (4, "Duplicate branch rewrite")]]
        files = {1: {"shader.rs"}, 2: {"shader.rs"}, 3: {"alloc.rs"}, 4: {"shader.rs"}}
        pairs = overlaps(prs, files, {1: ("patch", "tree"), 4: ("patch", "tree")})
        reasons = {tuple(p["prs"]): p["reason"] for p in pairs}
        self.assertEqual(reasons, {(1, 2): "shared issue", (1, 4): "same patch ID and merge tree",
                                   (2, 4): "shared issue"})

    def test_replays_only_a_recorded_resolution(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            repo = root / "repo"
            repo.mkdir()
            git(repo, "init", "--initial-branch=main")
            git(repo, "config", "user.email", "forge-test@example.invalid")
            git(repo, "config", "user.name", "Forge Test")

            def commit(contents):
                (repo / "source file.rs").write_text(contents + "\n", encoding="utf-8")
                git(repo, "add", "--", "source file.rs")
                git(repo, "commit", "-m", contents)
                return git(repo, "rev-parse", "HEAD").stdout.strip()

            base = commit("starting line")
            git(repo, "switch", "-c", "topic")
            head = commit("topic change")
            git(repo, "switch", "main")
            against = commit("main change")
            self.assertNotEqual(patch_id(repo, base, head), patch_id(repo, base, against))
            status = {"status": {"17": {"head": head, "against": against, "result": "conflicts with main"}}}

            first, remaining, _ = prepare_merge(repo, root / "first", status, 17)
            self.assertEqual(remaining, ["source file.rs"])
            (first / "source file.rs").write_text("reviewed result\n", encoding="utf-8")
            git(first, "-c", "rerere.enabled=true", "rerere")

            second, remaining, _ = prepare_merge(repo, root / "second", status, 17)
            self.assertEqual(remaining, [])
            self.assertEqual(git(second, "show", ":source file.rs").stdout, "reviewed result\n")
            self.assertEqual(git(second, "rev-parse", "HEAD").stdout.strip(), head)
            self.assertEqual(git(repo, "rev-parse", "HEAD").stdout.strip(), against)
            self.assertEqual(git(repo, "status", "--porcelain").stdout, "")

    def test_closure_is_a_preview_until_requested(self):
        head = "a" * 40
        target = {"state": "MERGED", "isDraft": False, "baseRefName": "main"}
        candidate = {"state": "OPEN", "headRefOid": head, "baseRefName": "main",
                     "labels": [{"name": "duplicate"}]}
        with patch("triage.github", side_effect=map(json.dumps, (target, candidate))) as gh:
            self.assertIn("Would close", close_duplicate("owner/repo", 1, 2, head))
            self.assertEqual(gh.call_count, 2)
        with patch("triage.github", side_effect=map(json.dumps, (target, {"permissions": {"push": False}}))) as gh:
            with self.assertRaisesRegex(ValueError, "write access"):
                close_duplicate("owner/repo", 1, 2, head, apply=True)
            self.assertEqual(gh.call_count, 2)
        with patch("triage.github", side_effect=map(json.dumps, (target, candidate | {"headRefOid": "b" * 40}))) as gh:
            with self.assertRaisesRegex(ValueError, "reviewed head"):
                close_duplicate("owner/repo", 1, 2, head)
            self.assertEqual(gh.call_count, 2)
        with patch("triage.github", side_effect=map(json.dumps, (target, candidate | {"labels": []}))):
            with self.assertRaisesRegex(ValueError, "duplicate label"):
                close_duplicate("owner/repo", 1, 2, head)
        with patch("triage.github", side_effect=map(json.dumps, (target, {"permissions": {"push": True}}, candidate, {}))) as gh:
            self.assertIn("Closed", close_duplicate("owner/repo", 1, 2, head, apply=True))
            gh.assert_called_with("pr", "close", "1", "-R", "owner/repo", "--comment",
                                  "Duplicate of #2. Please continue review there.")


if __name__ == "__main__":
    unittest.main()

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/has-sync-pr.py"


class ExistingSyncPRTest(unittest.TestCase):
    def run_query(self, pages, ref="main", exit_code=0):
        with tempfile.TemporaryDirectory() as directory:
            gh = Path(directory) / "gh"
            gh.write_text("#!/usr/bin/env python3\nimport sys\nprint(" + repr(json.dumps(pages)) + ")\nsys.exit(" + str(exit_code) + ")\n")
            gh.chmod(0o755)
            env = dict(os.environ, GITHUB_REPOSITORY="owner/docs", PATH=directory + ":" + os.environ["PATH"])
            return subprocess.run([sys.executable, str(SCRIPT), ref], env=env, capture_output=True, text=True)

    def test_existing_exact_ref_on_later_page_skips_new_pr(self):
        marker = "<!-- docs-sync-ref-sha256:" + hashlib.sha256(b"main").hexdigest() + " -->"
        result = self.run_query([[{"number": 1, "body": None}], [{"number": 7, "body": marker, "head": {"ref": "docs-sync/main", "repo": {"full_name": "owner/docs"}}}]])
        self.assertEqual(result.returncode, 0)
        self.assertIn("7", result.stdout)

    def test_different_ref_allows_new_pr(self):
        marker = "<!-- docs-sync-ref-sha256:" + hashlib.sha256(b"main").hexdigest() + " -->"
        self.assertEqual(self.run_query([[{"number": 7, "body": marker}]], ref="release").returncode, 1)

    def test_legacy_sync_pr_is_detected(self):
        pr = {"number": 8, "body": "old", "title": "Docs sync: print-handy@main", "head": {"ref": "docs-sync/main-123", "repo": {"full_name": "owner/docs"}}}
        self.assertEqual(self.run_query([[pr]]).returncode, 0)

    def test_existing_moving_ref_returns_branch_for_update(self):
        pr = {"number": 8, "body": "old", "title": "Docs sync: print-handy@main", "head": {"ref": "docs-sync/main", "repo": {"full_name": "owner/docs"}}}
        with tempfile.TemporaryDirectory() as directory:
            gh = Path(directory) / "gh"
            gh.write_text("#!/usr/bin/env python3\nimport sys\nprint(" + repr(json.dumps([[pr]])) + ")\n")
            gh.chmod(0o755)
            env = dict(os.environ, GITHUB_REPOSITORY="owner/docs", PATH=directory + ":" + os.environ["PATH"])
            result = subprocess.run([sys.executable, str(SCRIPT), "--branch", "main"], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "docs-sync/main")

    def test_matching_fork_pr_is_not_used_for_write_workflow(self):
        marker = "<!-- docs-sync-ref-sha256:" + hashlib.sha256(b"main").hexdigest() + " -->"
        pr = {"number": 9, "body": marker, "head": {"ref": "docs-sync/main", "repo": {"full_name": "attacker/docs"}}}
        self.assertEqual(self.run_query([[pr]]).returncode, 1)

    def test_unsafe_matching_branch_is_not_returned(self):
        marker = "<!-- docs-sync-ref-sha256:" + hashlib.sha256(b"main").hexdigest() + " -->"
        pr = {"number": 10, "body": marker, "head": {"ref": "docs-sync/main$(id)", "repo": {"full_name": "owner/docs"}}}
        self.assertEqual(self.run_query([[pr]]).returncode, 1)

    def test_api_failure_does_not_allow_creation(self):
        self.assertNotIn(self.run_query([], exit_code=2).returncode, (0, 1))


if __name__ == "__main__":
    unittest.main()

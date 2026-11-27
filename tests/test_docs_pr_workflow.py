from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocsPRWorkflowTest(unittest.TestCase):
    def test_docs_sync_approval_runs_for_human_named_sync_branches(self):
        workflow = (ROOT / ".github/workflows/docs-pr-check.yml").read_text()
        job = workflow.split("  docs-sync-approval:", 1)[1].split("  build:", 1)[0]

        self.assertIn("if: startsWith(github.event.pull_request.head.ref, 'docs-sync/')", job)
        self.assertNotIn("github.event.pull_request.user.login", job)

    def test_sync_workflow_dispatch_runs_checks_on_published_head(self):
        workflow = (ROOT / ".github/workflows/docs-pr-check.yml").read_text()
        auto_sync = (ROOT / ".github/workflows/docs-auto-sync.yml").read_text()

        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("inputs.sha", workflow)
        self.assertIn("ref: ${{ inputs.sha", workflow)
        self.assertIn("github.event_name == 'workflow_dispatch'", workflow)
        self.assertIn('gh workflow run docs-pr-check.yml', auto_sync)
        self.assertIn("actions: write", auto_sync)

    def test_legacy_sync_branch_without_sha_is_safe(self):
        workflow = (ROOT / ".github/workflows/docs-pr-check.yml").read_text()
        self.assertIn('if [ ! -f .docs-sync-upstream-sha ]; then', workflow)
        self.assertIn("Human review is required", workflow)


if __name__ == "__main__":
    unittest.main()

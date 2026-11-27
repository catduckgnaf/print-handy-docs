from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReviewedSyncTriggersTest(unittest.TestCase):
    def test_late_gates_retrigger_and_recheck_failed_build(self):
        workflow = (ROOT / '.github/workflows/merge-reviewed-sync.yml').read_text()
        self.assertIn('pull_request_review:', workflow)
        self.assertIn('pull_request:', workflow)
        self.assertIn('types: [edited]', workflow)
        self.assertNotIn('gh issue view 61', workflow)
        self.assertIn('gh run rerun "$run_id" --failed', workflow)
        self.assertIn('gh pr merge "$number" --squash --match-head-commit "$CHECKED_SHA"', workflow)
        self.assertIn('python3 scripts/validate_wiki_decisions.py', workflow)


if __name__ == '__main__':
    unittest.main()

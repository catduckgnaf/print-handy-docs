import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_wiki_decisions import validate


class WikiDecisionValidationTests(unittest.TestCase):
    def test_only_explicit_checked_decisions_pass(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n"
        self.assertEqual([], validate(body, ["GUIDE.md"]))

    def test_unchecked_or_placeholder_decisions_fail(self):
        for row in (
            "- [ ] `GUIDE.md` — wiki decision: `wiki-not-needed`",
            "- [x] `GUIDE.md` — wiki decision: **wiki-updated / wiki-not-needed** (record one)",
        ):
            with self.subTest(row=row):
                self.assertIn("missing explicit checked wiki decision", validate(row, ["GUIDE.md"]))

    def test_wiki_updated_needs_evidence(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated`\n"
        self.assertIn("must include a wiki page URL or revision", validate(body, ["GUIDE.md"]))

    def test_rejects_duplicate_decisions(self):
        body = ("- [x] `GUIDE.md` — wiki decision: `wiki-updated` — https://example.test/rev1\n"
                "- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n")
        self.assertIn("duplicate wiki decision", validate(body, ["GUIDE.md"]))

    def test_unrelated_issue_decisions_do_not_satisfy_guide(self):
        body = "- [x] `OTHER.md` — wiki decision: `wiki-not-needed`\n"
        self.assertIn("missing explicit checked wiki decision", validate(body, ["GUIDE.md"]))


if __name__ == "__main__":
    unittest.main()

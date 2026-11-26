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
                self.assertTrue(any("missing explicit checked wiki decision" in error for error in validate(row, ["GUIDE.md"])))

    def test_wiki_updated_needs_evidence(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated`\n"
        self.assertTrue(any("must include a wiki page URL or revision" in error for error in validate(body, ["GUIDE.md"])))

    def test_wiki_updated_rejects_arbitrary_evidence(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated` — done\n"
        self.assertTrue(any("must include a wiki page URL or revision" in error for error in validate(body, ["GUIDE.md"])))

    def test_wiki_updated_accepts_revision_evidence(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated` — abc1234\n"
        self.assertEqual([], validate(body, ["GUIDE.md"]))

    def test_rejects_duplicate_decisions(self):
        body = ("- [x] `GUIDE.md` — wiki decision: `wiki-updated` — https://example.test/rev1\n"
                "- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n")
        self.assertTrue(any("duplicate wiki decision" in error for error in validate(body, ["GUIDE.md"])))

    def test_unrelated_issue_decisions_do_not_satisfy_guide(self):
        body = "- [x] `OTHER.md` — wiki decision: `wiki-not-needed`\n"
        self.assertTrue(any("missing explicit checked wiki decision" in error for error in validate(body, ["GUIDE.md"])))


if __name__ == "__main__":
    unittest.main()

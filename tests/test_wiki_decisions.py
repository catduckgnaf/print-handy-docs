import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_wiki_decisions import validate, validate_reviews


def review(head, body, state="COMMENTED", association="COLLABORATOR"):
    return {"commit_id": head, "body": body, "state": state,
            "author_association": association, "submitted_at": "2026-01-01T00:00:00Z"}


class WikiDecisionValidationTests(unittest.TestCase):
    def test_review_provenance_rejects_marker_only_refresh(self):
        old, new = 'a' * 40, 'b' * 40
        row = '- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n'
        forged_body = f'<!-- wiki-assessment-head: {new} -->\n' + row
        self.assertTrue(validate_reviews([review(old, forged_body)], new, ['GUIDE.md']))
        self.assertEqual([], validate_reviews([review(new, row)], new, ['GUIDE.md']))
        self.assertTrue(validate_reviews([review(new, row, state='DISMISSED')], new, ['GUIDE.md']))
        self.assertTrue(validate_reviews([review(new, row, association='NONE')], new, ['GUIDE.md']))
        self.assertTrue(validate_reviews([review(new, row, state='CHANGES_REQUESTED')], new, ['GUIDE.md']))

    def test_new_cycle_needs_each_fresh_guide_decision(self):
        old = "- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n"
        fresh = "- [ ] `GUIDE.md` — wiki decision: `wiki-updated` — <wiki page URL or revision> OR `wiki-not-needed`\n"
        self.assertEqual([], validate(old, ["GUIDE.md"]))
        self.assertTrue(validate(fresh, ["GUIDE.md"]))
        self.assertTrue(validate(old, ["GUIDE.md", "OTHER.md"]))

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

    def test_wiki_updated_rejects_malformed_urls(self):
        for evidence in ("https://", "https://example.test", "https:///path", "https://user@example.test/wiki"):
            with self.subTest(evidence=evidence):
                body = f"- [x] `GUIDE.md` — wiki decision: `wiki-updated` — {evidence}\n"
                self.assertTrue(any("must include a wiki page URL or revision" in error for error in validate(body, ["GUIDE.md"])))

    def test_wiki_updated_accepts_page_url(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated` — https://example.test/wiki/GUIDE\n"
        self.assertEqual([], validate(body, ["GUIDE.md"]))

    def test_wiki_updated_accepts_revision_evidence(self):
        body = "- [x] `GUIDE.md` — wiki decision: `wiki-updated` — abc1234\n"
        self.assertEqual([], validate(body, ["GUIDE.md"]))

    def test_rejects_duplicate_decisions(self):
        body = ("- [x] `GUIDE.md` — wiki decision: `wiki-updated` — https://example.test/rev1\n"
                "- [x] `GUIDE.md` — wiki decision: `wiki-not-needed`\n")
        self.assertTrue(any("duplicate wiki decision" in error for error in validate(body, ["GUIDE.md"])))

    def test_guide_matching_ignores_path_and_case(self):
        body = "- [x] `docs/Standalone.md` — wiki decision: `wiki-not-needed`\n"
        self.assertEqual([], validate(body, ["STANDALONE.md"]))

    def test_normalized_duplicate_decisions_are_rejected(self):
        body = ("- [x] `docs/Standalone.md` — wiki decision: `wiki-not-needed`\n"
                "- [x] `STANDALONE.MD` — wiki decision: `wiki-not-needed`\n")
        self.assertTrue(any("duplicate wiki decision" in error for error in validate(body, ["standalone.md"])))

    def test_unrelated_issue_decisions_do_not_satisfy_guide(self):
        body = "- [x] `OTHER.md` — wiki decision: `wiki-not-needed`\n"
        self.assertTrue(any("missing explicit checked wiki decision" in error for error in validate(body, ["GUIDE.md"])))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Validate explicit per-guide wiki decisions recorded for the exact sync PR head."""
import argparse
import json
import re
import sys
from urllib.parse import urlparse

DECISION = re.compile(
    r"^- \[x\] `(?P<guide>[^`]+)` — wiki decision: `(?P<decision>wiki-updated|wiki-not-needed)`(?: — (?P<evidence>.+))?$",
    re.MULTILINE,
)


def valid_evidence(evidence: str) -> bool:
    if re.fullmatch(r"[0-9a-fA-F]{7,40}", evidence):
        return True
    parsed = urlparse(evidence)
    return (
        parsed.scheme in {"http", "https"}
        and bool(parsed.hostname)
        and "." in parsed.hostname
        and bool(parsed.path.strip("/"))
        and parsed.username is None
        and parsed.password is None
    )


def normalize_guide(guide: str) -> str:
    """Match source guide paths to site copies independent of path and case."""
    return guide.replace("\\", "/").rsplit("/", 1)[-1].casefold()


def validate(issue_body: str, guides: list[str]) -> list[str]:
    rows = {}
    for match in DECISION.finditer(issue_body):
        guide = match.group("guide")
        key = normalize_guide(guide)
        if key in rows:
            return [f"duplicate wiki decision for {guide}"]
        rows[key] = match.groupdict()
    errors = []
    for guide in guides:
        row = rows.get(normalize_guide(guide))
        if row is None:
            errors.append(f"missing explicit checked wiki decision for {guide}")
        elif row["decision"] == "wiki-updated" and not valid_evidence(row["evidence"] or ""):
            errors.append(f"wiki-updated for {guide} must include a wiki page URL or revision")
    return errors


def validate_reviews(reviews: list[dict], head: str, guides: list[str]) -> list[str]:
    """Require one complete assessment in a trusted, non-dismissed exact-head review.

    The commit_id is GitHub's review metadata, not text editable in the review.
    A review cannot combine partial decisions from different assessments.
    """
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        return ["invalid assessment head"]
    for review in reviews:
        if (review.get("commit_id") == head
                and review.get("state") in {"COMMENTED", "APPROVED"}
                and review.get("author_association") in {"OWNER", "MEMBER", "COLLABORATOR"}
                and review.get("submitted_at")
                and isinstance(review.get("body"), str)
                and not validate(review["body"], guides)):
            return []
    return ["no complete authorized wiki assessment review on exact head"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reviews", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--guides", nargs="+", required=True)
    args = parser.parse_args()
    with open(args.reviews, encoding="utf-8") as stream:
        reviews = json.load(stream)
    errors = validate_reviews(reviews, args.head, args.guides)
    if errors:
        print("Wiki decision validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated explicit wiki decisions for {len(args.guides)} guide(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

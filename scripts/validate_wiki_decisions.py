#!/usr/bin/env python3
"""Validate explicit per-guide wiki decisions recorded for the exact sync PR head."""
import argparse
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


def validate_head(body: str, head: str) -> list[str]:
    """Bind the entire assessment to one immutable sync PR commit."""
    markers = re.findall(r"^<!-- wiki-assessment-head: ([0-9a-f]{40}) -->$", body, re.MULTILINE)
    if not re.fullmatch(r"[0-9a-f]{40}", head) or markers != [head]:
        return ["missing, duplicate, or stale wiki assessment head"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue-body", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--guides", nargs="*", default=[])
    args = parser.parse_args()
    body = open(args.issue_body, encoding="utf-8").read()
    errors = validate_head(body, args.head) + validate(body, args.guides)
    if errors:
        print("Wiki decision validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated explicit wiki decisions for {len(args.guides)} guide(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate explicit per-guide wiki decisions recorded on Docs sync needed."""
import argparse
import re
import sys

DECISION = re.compile(
    r"^- \[x\] `(?P<guide>[^`]+)` — wiki decision: `(?P<decision>wiki-updated|wiki-not-needed)`(?: — (?P<evidence>.+))?$",
    re.MULTILINE,
)


def validate(issue_body: str, guides: list[str]) -> list[str]:
    rows = {}
    for match in DECISION.finditer(issue_body):
        guide = match.group("guide")
        if guide in rows:
            return [f"duplicate wiki decision for {guide}"]
        rows[guide] = match.groupdict()
    errors = []
    for guide in guides:
        row = rows.get(guide)
        if row is None:
            errors.append(f"missing explicit checked wiki decision for {guide}")
        elif row["decision"] == "wiki-updated" and not row["evidence"]:
            errors.append(f"wiki-updated for {guide} must include a wiki page URL or revision")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue-body", required=True)
    parser.add_argument("--guides", nargs="*", default=[])
    args = parser.parse_args()
    errors = validate(args.issue_body, args.guides)
    if errors:
        print("Wiki decision validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated explicit wiki decisions for {len(args.guides)} guide(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

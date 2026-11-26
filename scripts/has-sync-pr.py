#!/usr/bin/env python3
"""Find an open sync PR by an exact upstream-ref identity marker."""
import hashlib
import json
import os
import subprocess
import sys


def marker(ref):
    return "<!-- docs-sync-ref-sha256:" + hashlib.sha256(ref.encode()).hexdigest() + " -->"


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--marker":
        print(marker(sys.argv[2]))
        return 0
    if len(sys.argv) != 2:
        return 2
    repo = os.environ["GITHUB_REPOSITORY"]
    result = subprocess.run(
        ["gh", "api", "--paginate", "--slurp", f"repos/{repo}/pulls?state=open&per_page=100"],
        check=True, text=True, capture_output=True,
    )
    pages = json.loads(result.stdout)
    found = [pr["number"] for page in pages for pr in page
             if marker(sys.argv[1]) in (pr.get("body") or "")
             or (pr.get("title") == "Docs sync: print-handy@" + sys.argv[1]
                 and pr.get("head", {}).get("ref", "").startswith("docs-sync/"))]
    if found:
        print("Existing sync PR(s): " + ", ".join(map(str, found)))
        return 0
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (subprocess.SubprocessError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Cannot safely check open sync PRs: {exc}", file=sys.stderr)
        sys.exit(2)

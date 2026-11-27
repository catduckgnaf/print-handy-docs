#!/usr/bin/env python3
"""Fail closed unless the newest PR-specific check passed for this head."""
import json
import sys


def select(checks, runs, name, sha, number):
    suites = {
        run["check_suite_id"] for run in runs
        if run.get("event") in ("pull_request", "pull_request_review")
        and run.get("head_sha") == sha
        and any(pr.get("number") == number for pr in run.get("pull_requests", []))
    }
    eligible = [check for check in checks
                if check.get("name") == name
                and check.get("head_sha") == sha
                and (check.get("app") or {}).get("slug") == "github-actions"
                and (check.get("check_suite") or {}).get("id") in suites]
    latest = max(eligible, key=lambda c: (c.get("started_at") or "", c.get("id", 0)), default=None)
    return (latest.get("conclusion") or "pending") if latest else "missing"


def main():
    checks_path, runs_path, name, sha, number = sys.argv[1:]
    with open(checks_path) as f:
        checks = json.load(f)
    with open(runs_path) as f:
        runs = json.load(f)
    print(select(checks, runs, name, sha, int(number)))


if __name__ == "__main__":
    main()

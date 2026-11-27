import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHA = 'a' * 40


class DriftGateTest(unittest.TestCase):
    def test_review_event_drift_failure_and_dispatch_cannot_override(self):
        workflow = (ROOT / '.github/workflows/docs-pr-check.yml').read_text()
        step = workflow.split('      - name: Check sync PR against its recorded upstream commit\n', 1)[1].split('      - run: npm ci', 1)[0]
        condition = step.split('        if: ', 1)[1].splitlines()[0]
        # A review payload has pull_request.head.ref, but no github.head_ref.
        self.assertIn("startsWith(github.event.pull_request.head.ref, 'docs-sync/')", condition)
        self.assertNotIn('github.head_ref', condition)
        script = step.split('        run: |\n', 1)[1]
        script = '\n'.join(line[10:] for line in script.splitlines())
        merge = (ROOT / '.github/workflows/merge-reviewed-sync.yml').read_text()
        gate = merge.split("          for name in 'Build documentation'", 1)[1].split('          # Defend against', 1)[0]
        gate = "for name in 'Build documentation'" + gate.splitlines()[0] + '\n' + '\n'.join(line[10:] for line in gate.splitlines()[1:])
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            (d / 'scripts').mkdir()
            (d / 'bin').mkdir()
            (d / '.docs-sync-upstream-sha').write_text(SHA)
            (d / 'bin/git').write_text('#!/bin/sh\nif [ "$3" = rev-parse ]; then printf "%s\\n" "$TEST_SHA"; fi\nexit 0\n')
            (d / 'bin/git').chmod(0o755)
            check = d / 'scripts/check-sync.sh'
            check.write_text('#!/bin/sh\nexit "$DRIFT_STATUS"\n')
            check.chmod(0o755)
            env = dict(os.environ, PATH=str(d / 'bin') + ':' + os.environ['PATH'], RUNNER_TEMP=td,
                       GITHUB_STEP_SUMMARY=str(d / 'summary'), TEST_SHA=SHA)
            runs = [dict(check_suite_id=1, event='pull_request_review', head_sha=SHA, pull_requests=[dict(number=76)]),
                    dict(check_suite_id=2, event='workflow_dispatch', head_sha=SHA, pull_requests=[])]
            (d / 'runs.json').write_text(json.dumps(runs))
            for status, expected in [(1, 'failure'), (0, 'success')]:
                result = subprocess.run(['bash', '-c', script], cwd=d, env=dict(env, DRIFT_STATUS=str(status)), capture_output=True)
                self.assertEqual(result.returncode, status, result.stderr.decode())
                checks = [dict(id=1, name='Build documentation', head_sha=SHA, app=dict(slug='github-actions'), check_suite=dict(id=1), started_at='2026-01-01', conclusion=expected),
                          dict(id=2, name='Build documentation', head_sha=SHA, app=dict(slug='github-actions'), check_suite=dict(id=2), started_at='2026-01-02', conclusion='success'),
                          dict(id=3, name='docs-sync-approval', head_sha=SHA, app=dict(slug='github-actions'), check_suite=dict(id=1), started_at='2026-01-01', conclusion='success')]
                (d / 'checks.json').write_text(json.dumps(checks))
                # Execute the actual merge gate loop; a later dispatch success must not mask drift.
                command = 'cd "$REPO"; for attempt in 1; do\n' + gate + '\necho MERGE_ALLOWED; done'
                p = subprocess.run(['bash', '-c', command], env=dict(env, REPO=str(ROOT), CHECKED_SHA=SHA, number='76'), capture_output=True, text=True, timeout=5)
                self.assertEqual(p.returncode, 0, p.stderr)
                self.assertEqual('MERGE_ALLOWED' in p.stdout, status == 0, p.stdout)


if __name__ == '__main__':
    unittest.main()

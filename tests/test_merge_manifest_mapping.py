import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class MergeManifestMappingTest(unittest.TestCase):
    def run_mapping(self, paths, workflow_name='merge-reviewed-sync.yml'):
        workflow = (ROOT / '.github/workflows' / workflow_name).read_text()
        start = workflow.index('          changed_paths=')
        end = workflow.index('          mapfile -t guides', start)
        end = workflow.index('\n', end)
        block = '\n'.join(line[10:] for line in workflow[start:end].splitlines())
        script = 'set -euo pipefail\nnumber=123\nPR_NUMBER=123\nGH_REPO=owner/repo\ngh() { printf "%s\\n" "$CHANGED_PATHS"; }\n' + block + '\nprintf "%s\\n" "${guides[@]}"\n'
        return subprocess.run(['bash', '-c', script], cwd=ROOT, env={'PATH': '/usr/bin:/bin', 'CHANGED_PATHS': '\n'.join(paths)}, text=True, capture_output=True)

    def test_guide_uses_upstream_readme_name(self):
        for workflow in ('merge-reviewed-sync.yml', 'docs-pr-check.yml'):
            with self.subTest(workflow=workflow):
                result = self.run_mapping(['docs/guide.md', 'docs/diagnostics.md'], workflow)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(set(result.stdout.splitlines()), {'README.md', 'DIAGNOSTICS.md'})

    def test_unknown_guide_fails_closed(self):
        for workflow in ('merge-reviewed-sync.yml', 'docs-pr-check.yml'):
            with self.subTest(workflow=workflow):
                result = self.run_mapping(['docs/guide.md', 'docs/unmapped.md'], workflow)
                self.assertNotEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()

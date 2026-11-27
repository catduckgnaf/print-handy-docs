"""Exercise the workflow's branch checkout and three-dot guide discovery."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github/workflows/docs-auto-sync.yml'


def git(directory, *args):
    return subprocess.run(['git', '-C', str(directory), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


class SyncBranchHistoryTest(unittest.TestCase):
    def test_new_and_existing_branch_after_main_advances(self):
        workflow = WORKFLOW.read_text()
        checkout = workflow.split('- name: Checkout this docs repo', 1)[1].split('\n      - name:', 1)[0]
        full_history = 'fetch-depth: 0' in checkout
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            remote, seed, runner = root / 'remote.git', root / 'seed', root / 'runner'
            subprocess.run(['git', 'init', '--bare', '--initial-branch=main', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(seed)], check=True, capture_output=True)
            git(seed, 'config', 'user.name', 'Test')
            git(seed, 'config', 'user.email', 'test@example.invalid')
            (seed / 'base').write_text('base')
            git(seed, 'add', '.')
            git(seed, 'commit', '-m', 'base')
            git(seed, 'push', 'origin', 'main')
            git(seed, 'switch', '-c', 'docs-sync/existing')
            (seed / 'guide.md').write_text('changed guide')
            git(seed, 'add', '.')
            git(seed, 'commit', '-m', 'sync')
            git(seed, 'push', 'origin', 'docs-sync/existing')
            git(seed, 'switch', 'main')
            (seed / 'other').write_text('main advanced')
            git(seed, 'add', '.')
            git(seed, 'commit', '-m', 'advance main')
            git(seed, 'push', 'origin', 'main')
            clone = ['git', 'clone']
            if not full_history:
                clone += ['--depth', '1']
            subprocess.run(clone + [remote.as_uri(), str(runner)], check=True, capture_output=True)
            git(runner, 'switch', '-c', 'docs-sync/new')
            self.assertEqual(git(runner, 'diff', '--name-only', 'origin/main...HEAD'), '')
            git(runner, 'fetch', 'origin', 'docs-sync/existing')
            git(runner, 'switch', '-C', 'docs-sync/existing', 'FETCH_HEAD')
            self.assertEqual(git(runner, 'diff', '--name-only', 'origin/main...HEAD'), 'guide.md')


if __name__ == '__main__':
    unittest.main()

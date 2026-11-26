import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'sync-docs.py'


class StructuralChangeTest(unittest.TestCase):
    def run_case(self, added=False, removed=False):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / 'site'
            scripts = repo / 'scripts'
            docs = repo / 'docs'
            upstream = root / 'upstream' / 'docs'
            for directory in (scripts, docs, upstream):
                directory.mkdir(parents=True)
            shutil.copy2(SCRIPT, scripts / 'sync-docs.py')
            (scripts / 'check-sync.sh').write_text('EXCLUDE="IGNORED.md"\n')
            (scripts / 'sync-manifest.tsv').write_text('GUIDE.md\tguide.md\toldhash\n')
            (docs / 'guide.md').write_text('original site content\n')
            if not removed:
                (upstream / 'GUIDE.md').write_text('changed upstream content\n')
            if added:
                (upstream / 'NEW.md').write_text('# New guide\n')
            def snapshot():
                return {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in repo.rglob('*') if p.is_file()}
            before = snapshot()
            result = subprocess.run([sys.executable, str(scripts / 'sync-docs.py'),
                                     '--upstream', str(upstream.parent)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(before, snapshot())
            if added:
                self.assertIn('ADDED: NEW.md', result.stdout)
            if removed:
                self.assertIn('REMOVED: GUIDE.md', result.stdout)

    def test_added_guide_does_not_write(self):
        self.run_case(added=True)

    def test_removed_guide_does_not_write(self):
        self.run_case(removed=True)

    def test_added_and_removed_guides_do_not_write(self):
        self.run_case(added=True, removed=True)


if __name__ == '__main__':
    unittest.main()

import pathlib
import unittest


class MainSourceGuardTest(unittest.TestCase):
    def test_release_and_manual_runs_cannot_select_old_ref(self):
        workflow = pathlib.Path('.github/workflows/docs-auto-sync.yml').read_text()
        resolve = workflow.split('      - name: Resolve the upstream ref', 1)[1].split('      - name: Checkout upstream', 1)[0]
        self.assertIn('ref=main', resolve)
        self.assertIn('"$INPUT_REF" != main', resolve)
        self.assertNotIn('ref="${INPUT_REF:-$PAYLOAD_REF}"', resolve)
        self.assertNotIn('releases/latest', resolve)


if __name__ == '__main__':
    unittest.main()

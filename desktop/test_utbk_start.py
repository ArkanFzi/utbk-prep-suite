import unittest
import os
import subprocess

class TestUTBKStart(unittest.TestCase):
    def test_utbk_start_exists_and_executable(self):
        script_path = "/home/arkan/.local/bin/utbk-start"
        self.assertTrue(os.path.exists(script_path), "utbk-start script must exist")
        self.assertTrue(os.access(script_path, os.X_OK), "utbk-start must be executable")

    def test_utbk_start_dry_run(self):
        script_path = "/home/arkan/.local/bin/utbk-start"
        res = subprocess.run([script_path, "--dry-run"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("UTBK 2027", res.stdout)
        self.assertIn("Fokus", res.stdout)

if __name__ == "__main__":
    unittest.main()

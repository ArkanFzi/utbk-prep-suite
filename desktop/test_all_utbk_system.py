import unittest
import os

class TestAllUTBKSystem(unittest.TestCase):
    def test_all_deliverables(self):
        files = [
            "/home/arkan/Downloads/jadwal_utbk_2027.ics",
            "/home/arkan/Downloads/generate_utbk_ics.py",
            "/home/arkan/Downloads/utbk_reminder_linux.py",
            "/home/arkan/Downloads/anki_utbk2027_starter.csv",
            "/home/arkan/Downloads/panduan_anki_fsrs.md",
            "/home/arkan/Downloads/template_error_log_utbk.csv",
            "/home/arkan/Downloads/template_error_log_utbk.md",
            "/home/arkan/Downloads/PANDUAN_SETUP_SISTEM_UTBK.md"
        ]
        for f in files:
            self.assertTrue(os.path.exists(f), f"File {f} must exist")
            self.assertGreater(os.path.getsize(f), 50, f"File {f} must not be empty")

if __name__ == "__main__":
    unittest.main()

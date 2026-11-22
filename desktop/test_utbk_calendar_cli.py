import unittest
from datetime import date
import os
import json

class TestUTBKCalendarCLI(unittest.TestCase):
    def setUp(self):
        self.state_file = "/tmp/test_utbk_progress.json"
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def tearDown(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def test_get_agenda(self):
        import utbk_calendar_cli
        agenda = utbk_calendar_cli.get_agenda(date(2026, 11, 9), state_file=self.state_file)
        self.assertIn("Pengetahuan Kuantitatif", agenda["subtes"])
        self.assertEqual(agenda["status"], "TODO")

    def test_mark_done_and_streak(self):
        import utbk_calendar_cli
        # Mark done for today
        res = utbk_calendar_cli.mark_session_done(date(2026, 11, 9), state_file=self.state_file)
        self.assertTrue(res)

        agenda = utbk_calendar_cli.get_agenda(date(2026, 11, 9), state_file=self.state_file)
        self.assertEqual(agenda["status"], "DONE")

        stats = utbk_calendar_cli.get_stats(date(2026, 11, 9), state_file=self.state_file)
        self.assertEqual(stats["completed_sessions"], 1)

if __name__ == "__main__":
    unittest.main()

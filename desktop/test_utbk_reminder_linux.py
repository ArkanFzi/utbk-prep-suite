import unittest
from datetime import date
from unittest.mock import patch
import os

class TestUTBKReminderLinux(unittest.TestCase):
    def test_reminder_message_generation(self):
        import utbk_reminder_linux
        # Test Monday
        msg_mon = utbk_reminder_linux.get_today_reminder(date(2026, 11, 2))
        self.assertIsNotNone(msg_mon)
        self.assertIn("Pengetahuan Kuantitatif", msg_mon["subtes"])
        self.assertIn("19:30", msg_mon["time"])

        # Test Saturday
        msg_sat = utbk_reminder_linux.get_today_reminder(date(2026, 11, 7))
        self.assertIsNotNone(msg_sat)
        self.assertIn("Simulasi / Try-Out", msg_sat["subtes"])
        self.assertIn("09:00", msg_sat["time"])

    @patch("subprocess.run")
    def test_notify_send_execution(self, mock_subprocess):
        import utbk_reminder_linux
        success = utbk_reminder_linux.send_notification(
            title="Test Title",
            body="Test Body",
            dry_run=True
        )
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()

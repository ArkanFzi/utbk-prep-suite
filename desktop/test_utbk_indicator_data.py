import unittest
import os
import sys
import json
from datetime import date

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

class TestUTBKIndicatorData(unittest.TestCase):
    def test_countdown(self):
        import utbk_indicator_data
        days = utbk_indicator_data.get_countdown_days(date(2026, 11, 8))
        self.assertEqual(days, 164, "From 2026-11-08 to 2027-04-21 is 164 days")

    def test_today_schedule(self):
        import utbk_indicator_data
        sched = utbk_indicator_data.get_today_schedule(date(2026, 11, 8))
        self.assertIn("Review", sched["subtes"])
        self.assertIn("15:00", sched["time_str"])

    def test_formula_of_the_day(self):
        import utbk_indicator_data
        f1 = utbk_indicator_data.get_formula_of_the_day(date(2026, 11, 8))
        f2 = utbk_indicator_data.get_formula_of_the_day(date(2026, 11, 8))
        self.assertEqual(f1, f2, "Formula should be deterministic for same date")
        self.assertTrue(len(f1["front"]) > 5)
        self.assertTrue(len(f1["back"]) > 5)

    def test_topbar_label(self):
        import utbk_indicator_data
        label = utbk_indicator_data.get_topbar_label(date(2026, 11, 8))
        self.assertIn("H-164", label)
        self.assertIn("Review", label)

    def test_topbar_label_done(self):
        import utbk_indicator_data
        state_file = "/tmp/test_indicator_label_state.json"
        import json
        with open(state_file, "w") as f:
            json.dump({"completed_dates": ["2026-11-08"]}, f)

        try:
            label = utbk_indicator_data.get_topbar_label(date(2026, 11, 8), state_file=state_file)
            self.assertIn("DONE", label)
        finally:
            if os.path.exists(state_file):
                os.remove(state_file)

if __name__ == "__main__":
    unittest.main()

import unittest
import os

class TestUTBKIndicatorGUI(unittest.TestCase):
    def test_indicator_module_imports(self):
        import utbk_indicator
        self.assertTrue(hasattr(utbk_indicator, "build_menu"))
        self.assertTrue(hasattr(utbk_indicator, "update_indicator"))
        self.assertTrue(hasattr(utbk_indicator, "launch_utbk_start"))
        self.assertTrue(hasattr(utbk_indicator, "trigger_mobile_wallpaper"))
        self.assertTrue(hasattr(utbk_indicator, "trigger_checkin"))
        self.assertTrue(hasattr(utbk_indicator, "toggle_done"))
        self.assertTrue(hasattr(utbk_indicator, "toggle_focus_music"))

if __name__ == "__main__":
    unittest.main()

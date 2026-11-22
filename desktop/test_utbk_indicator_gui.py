import unittest
import os
import sys
from unittest.mock import MagicMock

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Mock gi repository in headless CI environments where GTK is not installed
try:
    import gi
except ImportError:
    gi = MagicMock()
    sys.modules["gi"] = gi
    sys.modules["gi.repository"] = MagicMock()
    sys.modules["gi.repository.Gtk"] = MagicMock()
    sys.modules["gi.repository.GLib"] = MagicMock()
    sys.modules["gi.repository.AyatanaAppIndicator3"] = MagicMock()
    sys.modules["gi.repository.AppIndicator3"] = MagicMock()

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

import unittest
from unittest.mock import patch, MagicMock

class TestUTBKMusicFocus(unittest.TestCase):
    def test_module_exports(self):
        import utbk_music_focus
        self.assertTrue(hasattr(utbk_music_focus, "is_spotify_running"))
        self.assertTrue(hasattr(utbk_music_focus, "get_playback_status"))
        self.assertTrue(hasattr(utbk_music_focus, "play_focus"))
        self.assertTrue(hasattr(utbk_music_focus, "pause"))
        self.assertTrue(hasattr(utbk_music_focus, "toggle_playback"))
        self.assertTrue(hasattr(utbk_music_focus, "set_volume"))

    @patch("subprocess.run")
    def test_pause_command(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        import utbk_music_focus
        res = utbk_music_focus.pause()
        self.assertTrue(res)

    @patch("subprocess.run")
    def test_set_volume(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        import utbk_music_focus
        res = utbk_music_focus.set_volume(0.4)
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()

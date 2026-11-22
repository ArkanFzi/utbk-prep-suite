import unittest
from datetime import date
import os
from PIL import Image

class TestMobileHUD(unittest.TestCase):
    def setUp(self):
        self.output_img = "/home/arkan/Downloads/utbk_mobile_lockscreen.png"
        if os.path.exists(self.output_img):
            os.remove(self.output_img)

    def test_generate_mobile_hud(self):
        import utbk_mobile_hud
        img_path = utbk_mobile_hud.generate_wallpaper(date(2026, 11, 9))
        self.assertTrue(os.path.exists(img_path))

        with Image.open(img_path) as img:
            self.assertEqual(img.size, (1080, 2400), "Should match vertical mobile resolution 1080x2400")

    def test_checkin_notification(self):
        import utbk_checkin_cron
        res = utbk_checkin_cron.send_checkin(date(2026, 11, 9), dry_run=True)
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()

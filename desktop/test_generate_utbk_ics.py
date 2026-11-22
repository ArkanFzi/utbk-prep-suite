import os
import unittest
from datetime import datetime

class TestUTBKCalendarGenerator(unittest.TestCase):
    def setUp(self):
        self.output_ics = "/home/arkan/Downloads/jadwal_utbk_2027.ics"
        if os.path.exists(self.output_ics):
            os.remove(self.output_ics)

    def test_ics_generation(self):
        import generate_utbk_ics
        generate_utbk_ics.main()

        self.assertTrue(os.path.exists(self.output_ics), "ICS file should be created")
        
        with open(self.output_ics, "r", encoding="utf-8") as f:
            content = f.read()

        # Check basic ICS structure
        self.assertIn("BEGIN:VCALENDAR", content)
        self.assertIn("END:VCALENDAR", content)
        self.assertIn("X-WR-CALNAME:UTBK 2027 - Target Informatika", content)
        
        # Check VALARM presence
        self.assertIn("BEGIN:VALARM", content)
        self.assertIn("-PT15M", content)
        
        # Check subtests presence
        self.assertIn("Pengetahuan Kuantitatif", content)
        self.assertIn("Penalaran Umum", content)
        self.assertIn("Penalaran Matematika", content)
        self.assertIn("Simulasi / Try-Out", content)
        
        # Check Milestones
        self.assertIn("Registrasi Akun SNPMB", content)
        self.assertIn("Pelaksanaan UTBK 2027", content)

        # Count events
        event_count = content.count("BEGIN:VEVENT")
        self.assertGreater(event_count, 150, "Should generate daily study sessions from Nov 2026 to Apr 2027 plus milestones")

if __name__ == "__main__":
    unittest.main()

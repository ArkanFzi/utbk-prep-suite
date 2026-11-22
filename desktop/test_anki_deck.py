import unittest
import csv
import os

class TestAnkiDeck(unittest.TestCase):
    def test_anki_csv_structure(self):
        csv_path = "/home/arkan/Downloads/anki_utbk2027_starter.csv"
        self.assertTrue(os.path.exists(csv_path), "Anki CSV file must exist")

        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [r for r in reader if r and not r[0].startswith("#")]

        # Ensure header + at least 15 starter cards
        self.assertGreaterEqual(len(rows), 15, "Should have at least 15 starter flashcards")
        
        subtests = set(r[2] for r in rows[1:])
        self.assertIn("PK", subtests)
        self.assertIn("PU", subtests)
        self.assertIn("PM", subtests)

if __name__ == "__main__":
    unittest.main()

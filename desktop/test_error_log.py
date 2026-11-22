import unittest
import csv
import os

class TestErrorLog(unittest.TestCase):
    def test_error_log_files(self):
        csv_path = "/home/arkan/Downloads/template_error_log_utbk.csv"
        md_path = "/home/arkan/Downloads/template_error_log_utbk.md"

        self.assertTrue(os.path.exists(csv_path), "CSV template should exist")
        self.assertTrue(os.path.exists(md_path), "Markdown template should exist")

        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
        
        expected_cols = ["No", "Tanggal_TO", "Subtes", "Topik_Materi", "Ringkasan_Soal", "Penyebab_Kesalahan", "Solusi_Kunci", "Status_Review", "Sudah_Dibuat_Anki"]
        for col in expected_cols:
            self.assertIn(col, header)

if __name__ == "__main__":
    unittest.main()

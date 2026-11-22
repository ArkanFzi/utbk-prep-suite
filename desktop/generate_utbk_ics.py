import uuid
from datetime import datetime, date, time, timedelta

MONTHLY_TOPICS = {
    (2026, 11, 1): {
        "PK": "Eksponen, Bentuk Akar, dan Pertidaksamaan Eksponensial",
        "PU": "Logika Proposisi (Negasi, Konjungsi, Disjungsi, Implikasi, Biimplikasi)",
        "PM": "Aritmatika Sosial (Persentase, Rasio, & Perbandingan Senilai/Berbalik Nilai)",
        "PK_PM": "Integrasi Eksponen & Aritmatika Sosial",
        "Lit": "LBIng Skimming & Main Idea",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 1",
        "Review": "Error Log Evaluasi Aljabar Dasar & Logika"
    },
    (2026, 11, 2): {
        "PK": "Persamaan & Pertidaksamaan Linear dan Kuadrat, Fungsi Kuadrat",
        "PU": "Ekuivalensi Implikasi (P -> Q = ~Q -> ~P = ~P or Q)",
        "PM": "Pemodelan Sistem Persamaan Linear (SPLDV & SPLTV)",
        "PK_PM": "Cross Drill: Persamaan Kuadrat & Model Cerita SPLDV",
        "Lit": "LBInd Analisis Paragraf & Kepaduan Kalimat",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 2",
        "Review": "Error Log Evaluasi SPLDV & Ekuivalensi Logika"
    },
    (2026, 11, 3): {
        "PK": "Fungsi, Komposisi Fungsi (f o g)(x), dan Fungsi Invers f^-1(x)",
        "PU": "Penarikan Kesimpulan Valid (Modus Ponens, Modus Tollens, Silogisme)",
        "PM": "Laju Perubahan & Perhitungan Diskon Bertingkat / Bunga",
        "PK_PM": "Cross Drill: Komposisi Fungsi & Laju Perubahan",
        "Lit": "LBIng Inference & Vocabulary in Context",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 3",
        "Review": "Error Log Evaluasi Fungsi & Silogisme"
    },
    (2026, 11, 4): {
        "PK": "Uji Konsep Aljabar Keseluruhan + Sifat Bilangan Rasional/Irasional",
        "PU": "Logika Analitis (Pengurutan & Posisi Duduk/Jadwal)",
        "PM": "Review Pemodelan Matematika & Aplikasi Keuangan",
        "PK_PM": "Cross Drill Aljabar & Logika Analitis",
        "Lit": "Speed Reading Teks Indonesia/Inggris + Try-Out 1 Evaluasi",
        "TO": "Try-Out 1 (Simulasi Evaluasi Bulanan November)",
        "Review": "Deep Review Error Log Try-Out 1"
    },
    (2026, 12, 1): {
        "PK": "Geometri Datar (Segitiga, Pythagoras, Kesebangunan, Luas & Keliling)",
        "PU": "Pola Deret Angka & Huruf (Larik 1, Larik 2, Bertingkat)",
        "PM": "Statistika Terapan (Mean, Median, Modus Data Kelompok)",
        "PK_PM": "Cross Drill: Geometri Datar & Analisis Data Terapan",
        "Lit": "LBInd Pemahaman PBM & Ejaan (PUEBI)",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 1 Des",
        "Review": "Error Log Geometri Datar & Pola Deret"
    },
    (2026, 12, 2): {
        "PK": "Geometri Ruang (Prisma, Tabung, Kerucut, Bola, Jarak & Volume)",
        "PU": "Pola Gambar 2D/3D (Rotasi, Matrix Pattern, Visual Reasoning)",
        "PM": "Ukuran Penyebaran (Jangkauan, Kuartil, Simpangan) & Perubahan Data Skalar",
        "PK_PM": "Cross Drill: Geometri Ruang & Ukuran Penyebaran Data",
        "Lit": "LBIng Reading Comprehension & Tone of the Author",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 2 Des",
        "Review": "Error Log Geometri Ruang & Visual Pattern"
    },
    (2026, 12, 3): {
        "PK": "Geometri Analitik (Persamaan Garis, Gradien, Garis Sejajar & Tegak Lurus)",
        "PU": "Analisis Teks (Pasti Benar, Mungkin Benar, Pasti Salah)",
        "PM": "Reading Charts & Graphs (Diagram Batang, Garis, Lingkaran)",
        "PK_PM": "Cross Drill: Geometri Garis & Grafik Batang/Garis",
        "Lit": "LBInd Menyunting Kalimat Efektif & Kohesi",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 3 Des",
        "Review": "Error Log Geometri Analitik & Analisis Teks"
    },
    (2026, 12, 4): {
        "PK": "Review Geometri Keseluruhan & Evaluasi Formatif",
        "PU": "Drill Campuran Penalaran Deduktif + Induktif",
        "PM": "Analisis Trend Data Kompleks & Ekstrapolasi",
        "PK_PM": "Cross Drill: Geometri & Trend Data",
        "Lit": "PBM & Literasi Try-Out 2 Evaluasi",
        "TO": "Try-Out 2 (Simulasi Evaluasi Bulanan Desember)",
        "Review": "Deep Review Error Log Try-Out 2"
    },
    (2027, 1, 1): {
        "PK": "Kaidah Pencacahan, Aturan Perkalian & Penjumlahan",
        "PU": "Pola Deret Fibonacci & Operasi Campuran Aritmatika Cepat",
        "PM": "Barisan & Deret Aritmatika Terapan",
        "PK_PM": "Cross Drill: Pencacahan & Barisan Aritmatika",
        "Lit": "LBIng Skimming Fast Reading & Scientific Tones",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 1 Jan",
        "Review": "Error Log Kaidah Pencacahan & Barisan Aritmatika"
    },
    (2027, 1, 2): {
        "PK": "Permutasi P(n,r) vs Kombinasi C(n,r)",
        "PU": "Penarikan Kuantitatif Dasar (Komparasi Kuantitas P dan Q)",
        "PM": "Barisan & Deret Geometri (Aplikasi Peluruhan & Pertumbuhan)",
        "PK_PM": "Cross Drill: Kombinasi & Deret Pertumbuhan",
        "Lit": "LBInd Makna Kata & Hubungan Sebab-Akibat",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 2 Jan",
        "Review": "Error Log Permutasi/Kombinasi & Deret Geometri"
    },
    (2027, 1, 3): {
        "PK": "Peluang Kejadian Tunggal, Majemuk, & Peluang Bersyarat",
        "PU": "Logika Simbolik & Operasi Matematika Buatan (Operator Baru)",
        "PM": "Deret Geometri Tak Hingga Terapan",
        "PK_PM": "Cross Drill: Peluang Bersyarat & Operator Baru",
        "Lit": "PBM Analisis Bentuk Kata & Imbuhan",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 3 Jan",
        "Review": "Error Log Peluang & Logika Simbolik"
    },
    (2027, 1, 4): {
        "PK": "Matriks (Operasi Dasar, Determinan, Invers)",
        "PU": "Review Penalaran Umum & Evaluasi Kecepatan Soal Deret/Silogisme",
        "PM": "Pemodelan Matriks dalam Sistem Persamaan",
        "PK_PM": "Cross Drill: Matriks & Sistem Persamaan",
        "Lit": "LBIng Reading Comprehension + TO 3",
        "TO": "Try-Out 3 (Evaluasi Mid-Roadmap Fase 1)",
        "Review": "Deep Review Error Log Try-Out 3 (Audit 3 Bulan)"
    },
    (2027, 2, 1): {
        "PK": "Speed Drill Tipe Soal Hubungan P vs Q & Kecukupan Data",
        "PU": "Trik Memecahkan Deret Kompleks dalam Waktu < 40 Detik",
        "PM": "Soal Cerita Kombinasi Aljabar + Geometri",
        "PK_PM": "Time-Attack PK & PM Soal Kecukupan Data",
        "Lit": "LBInd Analisis Struktur Teks Eksposisi & Argumentasi",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 1 Feb",
        "Review": "Error Log Speed Drill P vs Q & Deret Cepat"
    },
    (2027, 2, 2): {
        "PK": "Drill Soal Isian Singkat Kuantitatif (Akurasi Tanpa Opsi)",
        "PU": "Evaluasi Penalaran Deduktif Kompleks (Teks Panjang)",
        "PM": "Pemodelan Grafik & Tren Data Bisnis/Sains",
        "PK_PM": "Time-Attack Soal Isian Singkat & Grafik Tren",
        "Lit": "LBIng Inference & Detail Questions Strategy",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 2 Feb",
        "Review": "Error Log Isian Singkat Kuantitatif"
    },
    (2027, 2, 3): {
        "PK": "Variasi Soal Peluang & Kombinatorika UTBK Asli",
        "PU": "Penarikan Analitis Lanjutan (Kombinasi Syarat Batas)",
        "PM": "Optimasi Sederhana & Fungsi Kendala (Program Linear)",
        "PK_PM": "Cross Drill: Peluang & Program Linear",
        "Lit": "PBM & Ejaan Khusus Tanda Baca & Konjungsi",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 3 Feb",
        "Review": "Error Log Peluang & Syarat Batas Analitis"
    },
    (2027, 2, 4): {
        "PK": "Time-Attack Drill: 20 Soal PK dalam 25 Menit",
        "PU": "Time-Attack Drill: 30 Soal PU dalam 30 Menit",
        "PM": "Time-Attack Drill: 20 Soal PM dalam 30 Menit",
        "PK_PM": "Full Cross-Subtes Time Attack",
        "Lit": "LBIng Fast Scanning + Try-Out 4",
        "TO": "Try-Out 4 (Simulasi Speed & Pressure)",
        "Review": "Deep Review Error Log Try-Out 4"
    },
    (2027, 3, 1): {
        "PK": "Review Topik Kelemahan Utama Berdasarkan TO 1–4",
        "PU": "Bedah Soal PU Kuantitatif Berpola Rumit",
        "PM": "Soal Studi Kasus Matematika Keuangan & Distribusi Data",
        "PK_PM": "Drill Penguatan Titik Lemah Teridentifikasi",
        "Lit": "LBInd Strategi Scanning Soal Literasi Panjang",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 1 Mar",
        "Review": "Error Log Review Titik Lemah TO 1-4"
    },
    (2027, 3, 2): {
        "PK": "Drill Integrasi Aljabar, Fungsi, & Garis Lurus",
        "PU": "Speed Test Pola Gambar & Spatial Reasoning",
        "PM": "Pembahasan Soal HOTS Pemodelan Kompleks",
        "PK_PM": "Integrasi Aljabar-Fungsi & Soal HOTS",
        "Lit": "LBIng Reading Comprehension Complex Tones",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 2 Mar",
        "Review": "Error Log Soal HOTS & Pola Gambar"
    },
    (2027, 3, 3): {
        "PK": "Geometri Ruang & Peluang Kombinasi HOTS",
        "PU": "Latihan Konsistensi Logika (Menghindari Traps/Jebakan)",
        "PM": "Studi Kasus Soal Cerita Sains & Matematika Terapan",
        "PK_PM": "Drill Jebakan Logika & HOTS Geometri",
        "Lit": "Flash Drill: LBInd & PBM Ketelitian Tinggi",
        "TO": "Simulasi Latihan Soal Mandiri Minggu 3 Mar",
        "Review": "Error Log Jebakan Soal & Peluang HOTS"
    },
    (2027, 3, 4): {
        "PK": "Pemantapan Materi Kunci Prioritas Skor 700+",
        "PU": "Pemantapan Strategi Eliminasi Jawaban Cepat",
        "PM": "Pemantapan Trik Hitung Cepat Soal Cerita",
        "PK_PM": "Simulasi Mini Subtes Campuran",
        "Lit": "PBM & Literasi Speed Test + TO 5",
        "TO": "Try-Out 5 (Sistem IRT & Pembobotan Resmi)",
        "Review": "Deep Analysis Error Log TO 5 & Finalisasi Pilihan PTN"
    },
    (2027, 4, 1): {
        "PK": "Perbaikan 3 Topik Terlemah PK Berdasarkan TO 1-5",
        "PU": "Perbaikan Logika Deduktif & Analitis Terlemah",
        "PM": "Perbaikan Pemodelan Matematika Terlemah",
        "PK_PM": "Drill Tertarget Topik Lemah",
        "Lit": "Light Reading & Vocabulary Refresh",
        "TO": "Simulasi TO 6 (Full Subtes & Time Management)",
        "Review": "Evaluasi Strategi Alokasi Waktu per Subtes"
    },
    (2027, 4, 2): {
        "PK": "Drill Kecepatan Soal Menengah & Mudah (Zero Mistake)",
        "PU": "Pemantapan Pola Penalaran Umum Standar UTBK",
        "PM": "Drill Pemodelan Soal Mudah-Menengah",
        "PK_PM": "Latihan Strategi Skipping Soal Sulit (Risk Management)",
        "Lit": "Review Ringan Literasi Bahasa",
        "TO": "Simulasi TO 7 (Full Subtes Simulasi Terakhir)",
        "Review": "Review Final Error Log & Penguncian Pola Pikir"
    },
    (2027, 4, 3): {
        "PK": "Light Review Formula Sheet & Sifat Bilangan",
        "PU": "Light Review Aturan Logika & Silogisme",
        "PM": "Light Review Rumus-Rumus Dasar Statistika & Rasio",
        "PK_PM": "Mental Refresh & Review Catatan Ringkas (No Heavy Drill)",
        "Lit": "Bacaan Santai Bahasa Inggris & Indonesia",
        "TO": "Free Day / Rest - Jaga Kesehatan & Mood",
        "Review": "Pengecekan Berkas Fisik & Kartu Ujian SNBT"
    },
    (2027, 4, 4): {
        "PK": "PEAK PERFORMANCE: Ujian UTBK 2027",
        "PU": "PEAK PERFORMANCE: Ujian UTBK 2027",
        "PM": "PEAK PERFORMANCE: Ujian UTBK 2027",
        "PK_PM": "PEAK PERFORMANCE: Ujian UTBK 2027",
        "Lit": "PEAK PERFORMANCE: Ujian UTBK 2027",
        "TO": "HARI H PELAKSANAAN UTBK 2027 (21 - 30 APRIL 2027)",
        "Review": "Target Kelulusan S1/D4 Informatika (ITS / UB / POLINEMA)"
    }
}

MILESTONES = [
    {
        "summary": "📌 SNPMB: Registrasi Akun SNPMB (Siswa & Sekolah)",
        "desc": "Pastikan data NISN, NPSN, dan pasfoto valid di portal SNPMB.",
        "start": date(2027, 1, 12),
        "end": date(2027, 4, 7)
    },
    {
        "summary": "📌 SNBT: Pendaftaran & Pembayaran Biaya UTBK",
        "desc": "Pendaftaran UTBK SNBT 2027 & pemilihan prodi target (ITS / UB / POLINEMA). Jangan menunda sampai hari terakhir!",
        "start": date(2027, 3, 25),
        "end": date(2027, 4, 8)
    },
    {
        "summary": "📌 SNBT: Unduh & Cetak Kartu Peserta UTBK",
        "desc": "Cetak kartu ujian peserta UTBK, periksa sesi ujian (pagi/siang), cek lokasi pusat UTBK dan ruangan ujian.",
        "start": date(2027, 4, 11),
        "end": date(2027, 4, 15)
    },
    {
        "summary": "🎯 HARI H: Pelaksanaan UTBK 2027 (Peak Performance)",
        "desc": "Pelaksanaan tes UTBK SNBT 2027 resmi. Bawa kartu peserta, kartu identitas, dan perlengkapan ujian lengkap. Kerjakan soal dengan tenang dan terstruktur!",
        "start": date(2027, 4, 21),
        "end": date(2027, 4, 30)
    },
    {
        "summary": "🏆 SNBT: Pengumuman Hasil Kelulusan SNBT 2027",
        "desc": "Pengumuman hasil seleksi SNBT 2027. Cek di portal resmi SNPMB atau mirror PTN target.",
        "start": date(2027, 5, 25),
        "end": date(2027, 5, 25)
    }
]

def get_week_of_month(target_date: date) -> int:
    first_day = date(target_date.year, target_date.month, 1)
    day_num = target_date.day
    # 1-7: Week 1, 8-14: Week 2, 15-21: Week 3, 22+: Week 4
    week_num = min(4, ((day_num - 1) // 7) + 1)
    return week_num

def format_utc(dt: datetime) -> str:
    # WIB is UTC+7
    utc_dt = dt - timedelta(hours=7)
    return utc_dt.strftime("%Y%m%dT%H%M%SZ")

def format_date_only(d: date) -> str:
    return d.strftime("%Y%m%d")

def main():
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Antigravity AI//UTBK 2027 Scheduler//ID",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:UTBK 2027 - Target Informatika",
        "X-WR-TIMEZONE:Asia/Jakarta",
        "X-WR-CALDESC:Jadwal Belajar Intensif UTBK-SNBT 2027 Siswa SMK RPL (Target: ITS, UB, POLINEMA)"
    ]

    # Date range: 2026-11-01 to 2027-04-30
    curr_date = date(2026, 11, 1)
    end_date = date(2027, 4, 30)

    while curr_date <= end_date:
        weekday = curr_date.weekday() # 0: Mon, 1: Tue, ..., 6: Sun
        week_num = get_week_of_month(curr_date)
        key = (curr_date.year, curr_date.month, week_num)
        week_topics = MONTHLY_TOPICS.get(key, {})

        # Schedule rules:
        # Senin - Kamis: 19:30 - 21:00 (90 min)
        # Jumat: 20:00 - 21:30 (90 min)
        # Sabtu: 09:00 - 11:30 (150 min)
        # Minggu: 15:00 - 16:30 (90 min)
        
        session_info = None
        if weekday == 0:
            topic = week_topics.get("PK", "Pengetahuan Kuantitatif Bedah Konsep & Aljabar")
            session_info = {
                "subtes": "PK (Pengetahuan Kuantitatif)",
                "start_time": time(19, 30),
                "end_time": time(21, 0),
                "desc": f"Topik Minggu Ini: {topic}\\nIntensitas: High Focus\\nTarget: Bedah konsep & manipulasi rumus.",
                "color": "1" # Blue
            }
        elif weekday == 1:
            topic = week_topics.get("PU", "Penalaran Umum Logika & Deret")
            session_info = {
                "subtes": "PU (Penalaran Umum)",
                "start_time": time(19, 30),
                "end_time": time(21, 0),
                "desc": f"Topik Minggu Ini: {topic}\\nIntensitas: Medium Focus\\nTarget: Drill logika deduktif/induktif & kecepatan.",
                "color": "2" # Green
            }
        elif weekday == 2:
            topic = week_topics.get("PM", "Penalaran Matematika & Pemodelan")
            session_info = {
                "subtes": "PM (Penalaran Matematika)",
                "start_time": time(19, 30),
                "end_time": time(21, 0),
                "desc": f"Topik Minggu Ini: {topic}\\nIntensitas: High Focus\\nTarget: Abstraksi soal cerita & pemodelan persamaan.",
                "color": "5" # Yellow
            }
        elif weekday == 3:
            topic = week_topics.get("PK_PM", "Cross-Drill Soal Cerita & Geometri/Peluang")
            session_info = {
                "subtes": "PK & PM (Cross-Drill)",
                "start_time": time(19, 30),
                "end_time": time(21, 0),
                "desc": f"Topik Minggu Ini: {topic}\\nIntensitas: High Focus\\nTarget: Integrasi soal cerita & kecepatan eksekusi.",
                "color": "6" # Orange
            }
        elif weekday == 4:
            topic = week_topics.get("Lit", "Literasi Bahasa & Pemahaman PBM")
            session_info = {
                "subtes": "Literasi (LBIng & LBInd) / PBM",
                "start_time": time(20, 0),
                "end_time": time(21, 30),
                "desc": f"Topik Minggu Ini: {topic}\\nIntensitas: Light-Medium\\nTarget: Speed reading, main idea, & ketelitian kalimat.",
                "color": "3" # Purple
            }
        elif weekday == 5:
            topic = week_topics.get("TO", "Simulasi Try-Out Mandiri Full Subtes")
            session_info = {
                "subtes": "Simulasi / Try-Out",
                "start_time": time(9, 0),
                "end_time": time(11, 30),
                "desc": f"Sesi: {topic}\\nIntensitas: Maximum Focus\\nTarget: Pengerjaan soal dengan timer resmi ketat. Jangan buka pembahasan saat tes berlangsung!",
                "color": "11" # Red
            }
        elif weekday == 6:
            topic = week_topics.get("Review", "Evaluasi Error Log & Rest Mental")
            session_info = {
                "subtes": "Review Error Log & Rest",
                "start_time": time(15, 0),
                "end_time": time(16, 30),
                "desc": f"Sesi: {topic}\\nIntensitas: Low/Evaluasi\\nTarget: Input seluruh soal salah ke Error Log & konversi ke kartu flashcard Anki.",
                "color": "8" # Gray / Graphite
            }

        if session_info:
            dt_start = datetime.combine(curr_date, session_info["start_time"])
            dt_end = datetime.combine(curr_date, session_info["end_time"])
            uid = f"utbk-{curr_date.strftime('%Y%m%d')}-{session_info['start_time'].strftime('%H%M')}@antigravity"

            event_block = [
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{format_utc(datetime.now())}",
                f"DTSTART:{format_utc(dt_start)}",
                f"DTEND:{format_utc(dt_end)}",
                f"SUMMARY:UTBK 2027: {session_info['subtes']}",
                f"DESCRIPTION:{session_info['desc']}",
                "STATUS:CONFIRMED",
                "TRANSP:OPAQUE",
                "BEGIN:VALARM",
                "TRIGGER:-PT15M",
                "ACTION:DISPLAY",
                f"DESCRIPTION:Pengingat Sesi Belajar UTBK: {session_info['subtes']}",
                "END:VALARM",
                "END:VEVENT"
            ]
            ics_lines.extend(event_block)

        curr_date += timedelta(days=1)

    # Append Milestones
    for ms in MILESTONES:
        uid = f"ms-{ms['start'].strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}@antigravity"
        # All-day event
        end_inclusive = ms["end"] + timedelta(days=1)
        ms_block = [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{format_utc(datetime.now())}",
            f"DTSTART;VALUE=DATE:{format_date_only(ms['start'])}",
            f"DTEND;VALUE=DATE:{format_date_only(end_inclusive)}",
            f"SUMMARY:{ms['summary']}",
            f"DESCRIPTION:{ms['desc']}",
            "STATUS:CONFIRMED",
            "TRANSP:TRANSPARENT",
            "BEGIN:VALARM",
            "TRIGGER:-PT12H",
            "ACTION:DISPLAY",
            f"DESCRIPTION:Milestone Penting SNBT: {ms['summary']}",
            "END:VALARM",
            "END:VEVENT"
        ]
        ics_lines.extend(ms_block)

    ics_lines.append("END:VCALENDAR")
    
    output_path = "/home/arkan/Downloads/jadwal_utbk_2027.ics"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(ics_lines) + "\r\n")
    print(f"ICS successfully written to {output_path}")

if __name__ == "__main__":
    main()

# Panduan Lengkap Setup Sistem Belajar UTBK 2027 (Terintegrasi Linux & HP)

Sistem ini menghubungkan jadwal belajar dari laptop Linux ke smartphone kamu melalui **Google Calendar (`muhammadarkanfauzi9@gmail.com`)**, **Anki FSRS (Spaced Repetition)**, **Linux Desktop Reminder**, dan **Cloud Error Log**.

---

## 🚀 Langkah 1: Impor Jadwal ke Google Calendar (`muhammadarkanfauzi9@gmail.com`)

1. **Buka Google Calendar**:
   * Akses [calendar.google.com](https://calendar.google.com) di browser dan pastikan login dengan akun **`muhammadarkanfauzi9@gmail.com`**.
2. **Buat Kalender Khusus UTBK (Disarankan)**:
   * Di panel kiri, cari bagian **Other calendars** (Kalender lainnya), klik tanda **+** &rarr; pilih **Create new calendar** (Buat kalender baru).
   * Beri nama: `UTBK 2027` (Deskripsi: *Target Informatika ITS/UB/POLINEMA*).
   * Pilih warna aksen yang mencolok (misal merah, oranye, atau ungu).
3. **Impor File `.ics`**:
   * Buka menu **Settings** (ikon gerigi di kanan atas) &rarr; klik menu **Import & export** di bilah sisi kiri.
   * Pada bagian **Import**, klik **Select file from your computer**, lalu pilih file:
     ```
     /home/arkan/Downloads/jadwal_utbk_2027.ics
     ```
   * Pada kolom dropdown **Add to calendar**, pilih kalender `UTBK 2027` yang baru dibuat tadi (bukan kalender utama agar tidak bercampur).
   * Klik tombol **Import**.
4. **Hasil**:
   * Seluruh sesi belajar (Senin–Kamis 19:30, Jumat 20:00, Sabtu 09:00, Minggu 15:00) beserta topik mingguan dan milestone SNBT resmi langsung terdaftar sampai April 2027.
   * Alarm H-15 menit (19:15 WIB) otomatis berbunyi di aplikasi Google Calendar di HP Android/iOS kamu.

---

## 🔔 Langkah 2: Aktifkan Scheduler Pengingat Otomatis di Laptop Linux

Agar laptop yang sedang kamu gunakan ngoding memunculkan notifikasi pop-up otomatis di layar 15 menit sebelum sesi belajar:

1. Buka terminal di laptop dan jalankan:
   ```bash
   python3 /home/arkan/Downloads/utbk_reminder_linux.py --install-cron
   ```
2. Untuk menguji coba tampilan pop-up di layar laptop sekarang, jalankan:
   ```bash
   python3 /home/arkan/Downloads/utbk_reminder_linux.py
   ```
   *Laptop akan langsung menampilkan notifikasi desktop dengan judul subtes, topik materi hari ini, dan target belajar.*

---

## 🧠 Langkah 3: Setup Flashcard Interaktif Anki (FSRS) di Linux & HP

Untuk memastikan rumus PK/PM dan logika PU menempel permanen di memori jangka panjang:

1. **Pasang Anki di Linux & HP**:
   * **Linux**: `flatpak install flathub net.ankiweb.Anki` atau via Software Center.
   * **HP (Android)**: Install aplikasi **AnkiDroid** dari Google Play Store (Gratis).
2. **Impor Starter Deck**:
   * Di Anki Linux: Klik **Import File** &rarr; pilih `/home/arkan/Downloads/anki_utbk2027_starter.csv`.
   * Beri nama Deck: `UTBK 2027`.
3. **Aktifkan FSRS & Sinkronisasi**:
   * Buka **Deck Options** &rarr; aktifkan **FSRS** dengan target retensi `0.90` (90%).
   * Buat akun gratis di [ankiweb.net](https://ankiweb.net), lalu klik tombol **Sync** di laptop dan di HP.
   * *Detail panduan lengkap ada di file [`panduan_anki_fsrs.md`](file:///home/arkan/Downloads/panduan_anki_fsrs.md).*

---

## 📊 Langkah 4: Setup Cloud Error Log di Google Sheets / Notion

1. Buka [Google Sheets](https://sheets.new) di akun `muhammadarkanfauzi9@gmail.com`.
2. Klik menu **File** &rarr; **Import** &rarr; **Upload**, lalu pilih:
   ```
   /home/arkan/Downloads/template_error_log_utbk.csv
   ```
3. Pilih opsi **Replace current sheet**. Beri judul spreadsheet: `Error Log UTBK 2027`.
4. Pasang bookmark spreadsheet ini di browser laptop dan pasang shortcut di layar utama HP.
5. **Aturan Evaluasi**: Setiap kali salah soal saat latihan atau TO Sabtu, langsung catat ke tabel ini dan buat kartu flashcard barunya di Anki!

---

## 📁 Daftar File Sistem yang Siap Digunakan:

| File | Fungsi |
| :--- | :--- |
| [`jadwal_utbk_2027.ics`](file:///home/arkan/Downloads/jadwal_utbk_2027.ics) | Kalender universal untuk Google Calendar (HP & Web) |
| [`utbk_reminder_linux.py`](file:///home/arkan/Downloads/utbk_reminder_linux.py) | Skrip pengingat pop-up otomatis di layar laptop Linux |
| [`anki_utbk2027_starter.csv`](file:///home/arkan/Downloads/anki_utbk2027_starter.csv) | Bank flashcard rumus cepat PK, PM, & logika PU siap impor |
| [`panduan_anki_fsrs.md`](file:///home/arkan/Downloads/panduan_anki_fsrs.md) | Panduan aktivasi algoritma retensi memori FSRS |
| [`template_error_log_utbk.csv`](file:///home/arkan/Downloads/template_error_log_utbk.csv) | Template spreadsheet evaluasi soal salah mingguan |
| [`template_error_log_utbk.md`](file:///home/arkan/Downloads/template_error_log_utbk.md) | SOP klasifikasi akar masalah (Konsep, Teliti, Waktu) |

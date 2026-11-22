# 🎯 UTBK 2027 Study Suite

![Exam Target](https://img.shields.io/badge/Exam-UTBK--SNBT%202027-crimson?style=for-the-badge&logo=target)
![Target Program](https://img.shields.io/badge/Target-Informatika%20(ITS%20%7C%20UB%20%7C%20POLINEMA)-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20GNOME%20%2B%20Android%20PWA-success?style=for-the-badge)

Ekosistem persiapan belajar intensif UTBK-SNBT 2027 terpadu untuk siswa SMK RPL. Mengintegrasikan GNOME Top Bar Indicator (Linux), Interactive Web App (PWA), Direct USB Sync ke smartphone Android (Redmi 9A via ADB), dan Spaced Repetition (Anki FSRS).

---

## 🏗️ Struktur Repositori

```text
utbk-prep-suite/
├── desktop/         # Python Top Bar indicator (Ayatana), Spotify MPRIS, CLI timer
├── data/            # Database jadwal, file kalender (.ics), bank flashcard (.csv)
├── scripts/         # Script automasi sinkronisasi USB (ADB) ke HP Android
├── docs/            # Silabus subtes, panduan error log, dan roadmap materi
├── web/             # Interactive PWA Web App (Vite + React + Tailwind + Lucide)
├── .github/         # CI/CD GitHub Actions (Auto-deploy PWA ke GitHub Pages)
└── README.md        # Dokumentasi utama proyek
```

---

## ⚡ Fitur Utama

1. **GNOME Top Bar Indicator**:
   - Menampilkan countdown hari H-Day (`🎯 H-149`) dan status sesi hari ini langsung di panel atas desktop Linux.
   - Menu aksi 1-klik: Mulai Timer Belajar 90 Menit, Sinkronisasi Data ke HP (USB), dan Buka Web Dashboard.

2. **Interactive Web App & PWA**:
   - Focus Timer 90 Menit dengan indikator circular SVG.
   - Interactive 3D Formula Flip Card (Formula of the Day).
   - Error Log & Root Cause Classifier (Konsep, Teliti, Manajemen Waktu).
   - Offline-ready PWA untuk diinstal di layar utama smartphone.

3. **Direct USB Phone Sync (Redmi 9A via ADB)**:
   - Sekali colok kabel USB, jalankan `scripts/sync_phone_usb.sh` untuk otomatis push wallpaper lockscreen HUD, file kalender `.ics`, dan starter deck Anki ke HP.

4. **FSRS Spaced Repetition (Anki)**:
   - Terintegrasi dengan Anki Desktop & AnkiDroid untuk retensi jangka panjang rumus matematika PK/PM.

---

## 🚀 Panduan Menjalankan

### 1. Sinkronisasi Data ke HP via USB (ADB)
Pastikan HP terhubung via kabel USB dengan USB Debugging aktif:
```bash
./scripts/sync_phone_usb.sh
```

### 2. Menjalankan Web Dashboard Lokal
```bash
cd web
npm install
npm run dev
```

### 3. Mengaktifkan Top Bar Indicator (Linux)
```bash
systemctl --user restart utbk-indicator.service
```

---

## 📅 Roadmap Subtes Mingguan

- **Senin**: PK (Pengetahuan Kuantitatif) — *19:30 - 21:00 WIB*
- **Selasa**: PU (Penalaran Umum) — *19:30 - 21:00 WIB*
- **Rabu**: PM (Penalaran Matematika) — *19:30 - 21:00 WIB*
- **Kamis**: PK & PM (Cross-Drill Soal Cerita) — *19:30 - 21:00 WIB*
- **Jumat**: Literasi (Bahasa Indonesia & Inggris) — *20:00 - 21:30 WIB*
- **Sabtu**: Try-Out Simulasi Waktu Ketat — *09:00 - 11:30 WIB*
- **Minggu**: Bedah Error Log & Generate Flashcard — *15:00 - 16:30 WIB*

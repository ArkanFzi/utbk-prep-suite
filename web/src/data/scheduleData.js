export const WEEKDAY_SCHEDULE = {
  1: { // Senin
    subtest: "PK (Pengetahuan Kuantitatif)",
    code: "PK",
    color: "accentPk",
    badgeBg: "bg-red-500/10 text-red-400 border-red-500/30",
    time: "19:30 - 21:00 WIB",
    duration: 90,
    topic: "Bedah Konsep Aljabar, Eksponen & Persamaan Kuadrat",
    target: "Pahami fondasi manipulasi rumus cepat & hindari jebakan tanda."
  },
  2: { // Selasa
    subtest: "PU (Penalaran Umum)",
    code: "PU",
    color: "accentPu",
    badgeBg: "bg-emerald-500/10 text-emerald-400 border-emerald-500/30",
    time: "19:30 - 21:00 WIB",
    duration: 90,
    topic: "Drill Logika Deduktif, Silogisme & Pola Deret Angka",
    target: "Asah kecepatan analisis validitas kesimpulan premis."
  },
  3: { // Rabu
    subtest: "PM (Penalaran Matematika)",
    code: "PM",
    color: "accentPm",
    badgeBg: "bg-blue-500/10 text-blue-400 border-blue-500/30",
    time: "19:30 - 21:00 WIB",
    duration: 90,
    topic: "Pemodelan Soal Cerita, Rasio, & Aritmatika Sosial",
    target: "Terjemahkan teks naratif panjang menjadi model persamaan matematis."
  },
  4: { // Kamis
    subtest: "PK & PM (Cross-Drill)",
    code: "PK/PM",
    color: "accentPk",
    badgeBg: "bg-rose-500/10 text-rose-400 border-rose-500/30",
    time: "19:30 - 21:00 WIB",
    duration: 90,
    topic: "Cross-Drill Soal Cerita & Geometri / Peluang",
    target: "Kombinasi soal cerita dengan kecepatan hitung aritmatika."
  },
  5: { // Jumat
    subtest: "Literasi (LBIng & LBInd) / PBM",
    code: "Literasi",
    color: "accentLit",
    badgeBg: "bg-amber-500/10 text-amber-400 border-amber-500/30",
    time: "20:00 - 21:30 WIB",
    duration: 90,
    topic: "Speed Reading, Ide Pokok & Pemahaman Paragraf Kritis",
    target: "Teknik scanning & skimming tanpa kehilangan esensi makna paragraf."
  },
  6: { // Sabtu
    subtest: "Simulasi / Try-Out Mandiri",
    code: "Try-Out",
    color: "accentReview",
    badgeBg: "bg-purple-500/10 text-purple-400 border-purple-500/30",
    time: "09:00 - 11:30 WIB",
    duration: 150,
    topic: "Try-Out Mandiri Simulasi Waktu Ketat Resmi SNBT",
    target: "Full stamina, adaptasi kondisi ujian nyata tanpa membuka contekan!"
  },
  0: { // Minggu
    subtest: "Review Error Log & Rest",
    code: "Review",
    color: "accentPu",
    badgeBg: "bg-teal-500/10 text-teal-400 border-teal-500/30",
    time: "15:00 - 16:30 WIB",
    duration: 90,
    topic: "Bedah Soal Salah Mingguan & Konversi Kartu Anki",
    target: "Input semua blunder ke Error Log & kunci konsep di flashcard Anki."
  }
};

export const EXAM_TARGET_DATE = new Date("2027-04-21T07:00:00+07:00");

export function getCountdownDays() {
  const now = new Date();
  const diffTime = EXAM_TARGET_DATE - now;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return Math.max(0, diffDays);
}

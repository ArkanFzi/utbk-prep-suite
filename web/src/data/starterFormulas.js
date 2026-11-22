export const STARTER_FORMULAS = [
  {
    id: 1,
    subtest: "PK",
    subtestName: "Pengetahuan Kuantitatif",
    tag: "Aljabar Fondasi",
    front: "Apa syarat membalik tanda pertidaksamaan ketika menyelesaikan pertidaksamaan aljabar?",
    back: "Tanda pertidaksamaan (<, >, ≤, ≥) WAJIB DIBALIK jika kedua ruas dikali atau dibagi dengan bilangan negatif.\n\nContoh: -2x < 6 ⟹ x > -3."
  },
  {
    id: 2,
    subtest: "PK",
    subtestName: "Pengetahuan Kuantitatif",
    tag: "Persamaan Kuadrat",
    front: "Berapa rumus jumlah akar (x₁ + x₂) dan hasil kali akar (x₁ · x₂) dari ax² + bx + c = 0?",
    back: "• Jumlah akar: x₁ + x₂ = -b / a\n• Hasil kali akar: x₁ · x₂ = c / a\n• Selisih kuadrat: |x₁ - x₂| = √D / a  (di mana D = b² - 4ac)"
  },
  {
    id: 3,
    subtest: "PK",
    subtestName: "Pengetahuan Kuantitatif",
    tag: "Fungsi Invers",
    front: "Bagaimana rumus cepat invers fungsi pecahan linear f(x) = (ax + b) / (cx + d)?",
    back: "f⁻¹(x) = (-dx + b) / (cx - a)\n\nTrik: Tukar posisi a dan d, lalu beri tanda minus (-). Posisi b dan c tetap."
  },
  {
    id: 4,
    subtest: "PK",
    subtestName: "Pengetahuan Kuantitatif",
    tag: "Geometri Triples",
    front: "Sebutkan 5 kombinasi Triple Pythagoras yang paling sering muncul di UTBK!",
    back: "1. 3, 4, 5 (dan kelipatannya: 6,8,10 / 9,12,15)\n2. 5, 12, 13 (kelipatan: 10,24,26)\n3. 7, 24, 25\n4. 8, 15, 17\n5. 9, 40, 41"
  },
  {
    id: 5,
    subtest: "PK",
    subtestName: "Pengetahuan Kuantitatif",
    tag: "Trigonometri Sudut Istimewa",
    front: "Berapa rasio sisi-sisi pada segitiga siku-siku dengan sudut 30° - 60° - 90°?",
    back: "Rasio sisi (di depan 30° : 60° : 90°) adalah:\n1 : √3 : 2\n\n(Sisi terpendek = 1 di depan 30°, hipotenusa = 2 di depan 90°)"
  },
  {
    id: 6,
    subtest: "PU",
    subtestName: "Penalaran Umum",
    tag: "Logika Implikasi",
    front: "Apa ekuivalensi dari pernyataan implikasi (P ⟹ Q)?",
    back: "P ⟹ Q ekuivalen (≡) dengan:\n1. ~Q ⟹ ~P (Kontraposisi)\n2. ~P ∨ Q (Disjungsi ingkaran P)\n\nJebakan: P ⟹ Q TIDAK ekuivalen dengan Q ⟹ P (Konvers) maupun ~P ⟹ ~Q (Invers)!"
  },
  {
    id: 7,
    subtest: "PU",
    subtestName: "Penalaran Umum",
    tag: "Logika Negasi",
    front: "Apa bentuk negasi dari implikasi (P ⟹ Q)?",
    back: "~(P ⟹ Q) ≡ P ∧ ~Q\n\nArtinya: 'Premis P terjadi, DAN kesimpulan Q TIDAK terjadi'."
  },
  {
    id: 8,
    subtest: "PU",
    subtestName: "Penalaran Umum",
    tag: "Logika Silogisme",
    front: "Jelaskan aturan Modus Ponens dan Modus Tollens dalam penarikan kesimpulan!",
    back: "Modus Ponens:\nPremis 1: P ⟹ Q\nPremis 2: P\nKesimpulan: Q\n\nModus Tollens:\nPremis 1: P ⟹ Q\nPremis 2: ~Q\nKesimpulan: ~P"
  },
  {
    id: 9,
    subtest: "PU",
    subtestName: "Penalaran Umum",
    tag: "Logika Kuantor",
    front: "Apa ingkaran/negasi dari pernyataan kuantor universal 'Semua siswa SMK lulus ujian'?",
    back: "Ingkaran 'Semua A adalah B' adalah 'Ada / Beberapa A yang BUKAN B'.\n\nNegasi: 'Ada (minimal satu) siswa SMK yang tidak lulus ujian'."
  },
  {
    id: 10,
    subtest: "PM",
    subtestName: "Penalaran Matematika",
    tag: "Aritmatika Sosial",
    front: "Bagaimana menghitung diskon bertingkat d₁% dilanjutkan d₂%?",
    back: "Total persen bayar: (100 - d₁)% × (100 - d₂)%\nTotal diskon riil: 1 - (1 - d₁)(1 - d₂)\n\nContoh: Diskon 50% + 20% ⟹ Bayar 40% ⟹ Total Diskon 60% (BUKAN 70%!)."
  },
  {
    id: 11,
    subtest: "PM",
    subtestName: "Penalaran Matematika",
    tag: "Statistika Cepat",
    front: "Apa rumus nilai rata-rata gabungan dari dua kelompok data?",
    back: "x̄_gab = (n₁ · x̄₁ + n₂ · x̄₂) / (n₁ + n₂)\n\nTrik Tuas: Rasio selisih rata-rata berbanding terbalik dengan jumlah anggota:\nn₁ / n₂ = |x̄₂ - x̄_gab| / |x̄₁ - x̄_gab|"
  },
  {
    id: 12,
    subtest: "PM",
    subtestName: "Penalaran Matematika",
    tag: "Deret Geometri",
    front: "Apa rumus deret geometri tak hingga yang konvergen (|r| < 1) dan aplikasi bola jatuh?",
    back: "• S_∞ = a / (1 - r)\n• Aplikasi Pantulan Bola dari tinggi h rasio r:\nTotal Lintasan = h × (1 + r) / (1 - r)"
  },
  {
    id: 13,
    subtest: "PM",
    subtestName: "Penalaran Matematika",
    tag: "Pekerjaan Bersama",
    front: "Kapan suatu masalah pekerjaan bersama diselesaikan dengan rumus berbalik nilai?",
    back: "1/t_total = 1/t_A + 1/t_B\n\nRumus Cepat 2 Orang: t_total = (t_A · t_B) / (t_A + t_B)"
  }
];

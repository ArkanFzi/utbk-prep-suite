import os
import csv
import json
import re
from datetime import date

# Import schedule metadata from existing generator
from generate_utbk_ics import MONTHLY_TOPICS, get_week_of_month

EXAM_DATE = date(2027, 4, 21)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANKI_CSV = os.path.join(PROJECT_ROOT, "data", "anki_utbk2027_starter.csv")
if not os.path.exists(ANKI_CSV):
    ANKI_CSV = "/home/arkan/Downloads/anki_utbk2027_starter.csv"
DEFAULT_PROGRESS_FILE = os.path.expanduser("~/.local/share/utbk_progress.json")

def get_countdown_days(target_date: date = None) -> int:
    if target_date is None:
        target_date = date.today()
    delta = EXAM_DATE - target_date
    return delta.days

def get_today_schedule(target_date: date = None) -> dict:
    if target_date is None:
        target_date = date.today()

    weekday = target_date.weekday()
    week_num = get_week_of_month(target_date)
    key = (target_date.year, target_date.month, week_num)
    week_topics = MONTHLY_TOPICS.get(key, {})

    mapping = {
        0: {
            "subtes": "PK (Pengetahuan Kuantitatif)",
            "short_code": "PK",
            "time_str": "19:30 - 21:00 WIB",
            "start_time": "19:30",
            "topic": week_topics.get("PK", "Bedah Konsep Aljabar & Eksponen"),
            "target": "Bedah konsep & manipulasi rumus cepat."
        },
        1: {
            "subtes": "PU (Penalaran Umum)",
            "short_code": "PU",
            "time_str": "19:30 - 21:00 WIB",
            "start_time": "19:30",
            "topic": week_topics.get("PU", "Drill Logika Deduktif & Silogisme"),
            "target": "Kecepatan analisis deret & validitas kesimpulan."
        },
        2: {
            "subtes": "PM (Penalaran Matematika)",
            "short_code": "PM",
            "time_str": "19:30 - 21:00 WIB",
            "start_time": "19:30",
            "topic": week_topics.get("PM", "Pemodelan Soal Cerita & Rasio"),
            "target": "Abstraksi soal cerita ke persamaan matematika."
        },
        3: {
            "subtes": "PK & PM (Cross-Drill)",
            "short_code": "PK/PM",
            "time_str": "19:30 - 21:00 WIB",
            "start_time": "19:30",
            "topic": week_topics.get("PK_PM", "Cross Drill Soal Cerita & Geometri/Peluang"),
            "target": "Kombinasi soal cerita & kecepatan berhitung."
        },
        4: {
            "subtes": "Literasi (LBIng & LBInd) / PBM",
            "short_code": "Literasi",
            "time_str": "20:00 - 21:30 WIB",
            "start_time": "20:00",
            "topic": week_topics.get("Lit", "Speed Reading & Pemahaman Paragraf"),
            "target": "Scanning cepat kalimat efektif & ide pokok."
        },
        5: {
            "subtes": "Simulasi / Try-Out",
            "short_code": "Try-Out",
            "time_str": "09:00 - 11:30 WIB",
            "start_time": "09:00",
            "topic": week_topics.get("TO", "Try-Out Mandiri Simulasi Waktu Ketat"),
            "target": "Full fokus, simulasi real-time tanpa jeda!"
        },
        6: {
            "subtes": "Review Error Log & Rest",
            "short_code": "Review",
            "time_str": "15:00 - 16:30 WIB",
            "start_time": "15:00",
            "topic": week_topics.get("Review", "Input Soal Salah & Generate Anki"),
            "target": "Bedah soal salah minggu ini & konversi ke kartu Anki."
        }
    }
    return mapping.get(weekday, {
        "subtes": "Istirahat / Evaluasi",
        "short_code": "Rest",
        "time_str": "-",
        "start_time": "-",
        "topic": "Free Time",
        "target": "Recharge stamina."
    })

def clean_html(raw_html: str) -> str:
    clean = re.sub(r'<br\s*/?>', '\n', raw_html)
    clean = re.sub(r'<[^>]+>', '', clean)
    clean = clean.replace('&lt;', '<').replace('&gt;', '>').replace('&le;', '<=').replace('&ge;', '>=')
    clean = clean.replace('&sup2;', '²').replace('&radic;', '√').replace('&equiv;', '≡').replace('&and;', '∧').replace('&or;', '∨').replace('&times;', '×')
    clean = clean.replace('&rArr;', '⇒').replace('&ne;', '≠').replace('&infin;', '∞')
    return clean.strip()

def get_formula_of_the_day(target_date: date = None) -> dict:
    if target_date is None:
        target_date = date.today()

    cards = []
    if os.path.exists(ANKI_CSV):
        with open(ANKI_CSV, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and not row[0].startswith("#") and len(row) >= 3 and row[0] != "Front":
                    cards.append({
                        "front": clean_html(row[0]),
                        "back": clean_html(row[1]),
                        "subtest": row[2]
                    })

    if not cards:
        return {
            "front": "f(x) = (ax + b) / (cx + d)",
            "back": "f^-1(x) = (-dx + b) / (cx - a)",
            "subtest": "PK"
        }

    # Deterministic index based on date
    day_hash = (target_date.year * 1000 + target_date.timetuple().tm_yday)
    card = cards[day_hash % len(cards)]
    return card

def get_topbar_label(target_date: date = None, state_file: str = None) -> str:
    if target_date is None:
        target_date = date.today()

    days = get_countdown_days(target_date)
    sched = get_today_schedule(target_date)

    progress_file = state_file or DEFAULT_PROGRESS_FILE
    is_done = False
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if target_date.strftime("%Y-%m-%d") in data.get("completed_dates", []):
                    is_done = True
        except Exception:
            pass

    if is_done:
        return f"🎯 H-{days} | [DONE ✓]"

    return f"🎯 H-{days} | {sched['start_time']} {sched['short_code']}"

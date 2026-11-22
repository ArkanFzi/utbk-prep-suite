#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, "/home/arkan/Downloads")

import json
import argparse
from datetime import date, datetime, timedelta

from utbk_indicator_data import (
    get_countdown_days,
    get_today_schedule,
    get_formula_of_the_day,
    EXAM_DATE
)

DEFAULT_STATE_FILE = os.path.expanduser("~/.local/share/utbk_progress.json")

def load_progress(state_file: str = None) -> dict:
    target_file = state_file or DEFAULT_STATE_FILE
    if os.path.exists(target_file):
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed_dates": [], "streaks": 0}

def save_progress(data: dict, state_file: str = None):
    target_file = state_file or DEFAULT_STATE_FILE
    os.makedirs(os.path.dirname(os.path.abspath(target_file)), exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_agenda(target_date: date = None, state_file: str = None) -> dict:
    if target_date is None:
        target_date = date.today()

    sched = get_today_schedule(target_date)
    progress = load_progress(state_file)

    date_str = target_date.strftime("%Y-%m-%d")
    is_done = date_str in progress.get("completed_dates", [])

    return {
        "date": date_str,
        "days_left": get_countdown_days(target_date),
        "subtes": sched["subtes"],
        "short_code": sched["short_code"],
        "time_str": sched["time_str"],
        "topic": sched["topic"],
        "target": sched["target"],
        "status": "DONE" if is_done else "TODO"
    }

def mark_session_done(target_date: date = None, state_file: str = None) -> bool:
    if target_date is None:
        target_date = date.today()

    progress = load_progress(state_file)
    date_str = target_date.strftime("%Y-%m-%d")

    completed = set(progress.get("completed_dates", []))
    completed.add(date_str)
    progress["completed_dates"] = sorted(list(completed))

    save_progress(progress, state_file)
    return True

def get_stats(target_date: date = None, state_file: str = None) -> dict:
    if target_date is None:
        target_date = date.today()

    progress = load_progress(state_file)
    completed = set(progress.get("completed_dates", []))

    # Calculate streak ending today or yesterday
    streak = 0
    check_d = target_date
    if check_d.strftime("%Y-%m-%d") not in completed:
        check_d -= timedelta(days=1)

    while check_d.strftime("%Y-%m-%d") in completed:
        streak += 1
        check_d -= timedelta(days=1)

    return {
        "completed_sessions": len(completed),
        "current_streak": streak,
        "days_until_exam": get_countdown_days(target_date)
    }

def print_agenda_cli(target_date: date = None, state_file: str = None):
    agenda = get_agenda(target_date, state_file)
    status_badge = "\033[92m[DONE ✓]\033[0m" if agenda["status"] == "DONE" else "\033[93m[TODO ⌛]\033[0m"

    print(f"\n\033[1;36m====================================================\033[0m")
    print(f" 🎯 \033[1mUTBK 2027 AGENDA\033[0m | H-{agenda['days_left']} Hari (21 Apr 2027)")
    print(f" 📅 Tanggal: {agenda['date']}  | Status: {status_badge}")
    print(f"\033[1;36m====================================================\033[0m")
    print(f" ⏰ \033[1mWaktu Sesi\033[0m  : {agenda['time_str']}")
    print(f" 📚 \033[1mSubtes\033[0m      : {agenda['subtes']}")
    print(f" 📝 \033[1mMateri Fokus\033[0m: {agenda['topic']}")
    print(f" 🎯 \033[1mTarget\033[0m      : {agenda['target']}")
    print(f"\033[1;36m----------------------------------------------------\033[0m")

    formula = get_formula_of_the_day(target_date)
    print(f" 💡 \033[1;33mFormula of the Day ({formula['subtest']}):\033[0m")
    print(f"    ❓ {formula['front']}")
    print(f"    👉 \033[92m{formula['back']}\033[0m")
    print(f"\033[1;36m====================================================\033[0m\n")

def main():
    parser = argparse.ArgumentParser(description="UTBK 2027 Study Schedule CLI")
    parser.add_argument("command", nargs="?", default="agenda", choices=["agenda", "done", "stats"], help="Action to perform")
    parser.add_argument("--date", help="Specific date YYYY-MM-DD")
    args = parser.parse_args()

    target_d = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today()

    if args.command == "agenda":
        print_agenda_cli(target_d)
    elif args.command == "done":
        mark_session_done(target_d)
        print(f"\033[92m✓ Berhasil! Sesi belajar tanggal {target_d} ditandai [DONE].\033[0m")
        print_agenda_cli(target_d)
    elif args.command == "stats":
        stats = get_stats(target_d)
        print(f"\n📊 \033[1mStatistik Belajar UTBK 2027\033[0m:")
        print(f"   • Sesi Selesai : \033[1;32m{stats['completed_sessions']}\033[0m sesi")
        print(f"   • Current Streak: \033[1;33m{stats['current_streak']}\033[0m hari berturut-turut")
        print(f"   • Sisa Waktu   : \033[1;36m{stats['days_until_exam']}\033[0m hari menuju ujian\n")

if __name__ == "__main__":
    main()

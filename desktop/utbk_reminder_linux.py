import os
import sys
import subprocess
from datetime import date, datetime
import argparse

# Import schedule metadata
from generate_utbk_ics import MONTHLY_TOPICS, get_week_of_month

def get_today_reminder(target_date: date = None):
    if target_date is None:
        target_date = date.today()

    weekday = target_date.weekday()
    week_num = get_week_of_month(target_date)
    key = (target_date.year, target_date.month, week_num)
    week_topics = MONTHLY_TOPICS.get(key, {})

    schedule_map = {
        0: {
            "subtes": "PK (Pengetahuan Kuantitatif)",
            "time": "19:30 - 21:00 WIB",
            "topic": week_topics.get("PK", "Bedah Konsep Aljabar & Eksponen"),
            "target": "Target: Bedah konsep & manipulasi rumus cepat."
        },
        1: {
            "subtes": "PU (Penalaran Umum)",
            "time": "19:30 - 21:00 WIB",
            "topic": week_topics.get("PU", "Drill Logika Deduktif & Silogisme"),
            "target": "Target: Kecepatan analisis deret & validitas kesimpulan."
        },
        2: {
            "subtes": "PM (Penalaran Matematika)",
            "time": "19:30 - 21:00 WIB",
            "topic": week_topics.get("PM", "Pemodelan Soal Cerita & Rasio"),
            "target": "Target: Abstraksi soal cerita ke persamaan matematika."
        },
        3: {
            "subtes": "PK & PM (Cross-Drill)",
            "time": "19:30 - 21:00 WIB",
            "topic": week_topics.get("PK_PM", "Cross Drill Soal Cerita & Geometri/Peluang"),
            "target": "Target: Kombinasi soal cerita & kecepatan berhitung."
        },
        4: {
            "subtes": "Literasi (LBIng & LBInd) / PBM",
            "time": "20:00 - 21:30 WIB",
            "topic": week_topics.get("Lit", "Speed Reading & Pemahaman Paragraf"),
            "target": "Target: Scanning cepat kalimat efektif & ide pokok."
        },
        5: {
            "subtes": "Simulasi / Try-Out",
            "time": "09:00 - 11:30 WIB",
            "topic": week_topics.get("TO", "Try-Out Mandiri Simulasi Waktu Ketat"),
            "target": "Target: Full fokus, simulasi real-time tanpa jeda!"
        },
        6: {
            "subtes": "Review Error Log & Rest",
            "time": "15:00 - 16:30 WIB",
            "topic": week_topics.get("Review", "Input Soal Salah & Generate Anki"),
            "target": "Target: Bedah soal salah minggu ini & konversi ke kartu Anki."
        }
    }

    return schedule_map.get(weekday)

def send_notification(title: str, body: str, dry_run: bool = False) -> bool:
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {title}\n{body}")
    if dry_run:
        return True

    env = os.environ.copy()
    uid = os.getuid()
    if not env.get("DISPLAY"):
        env["DISPLAY"] = ":1" if os.path.exists("/tmp/.X11-unix/X1") else ":0"
    if not env.get("DBUS_SESSION_BUS_ADDRESS"):
        dbus_path = f"/run/user/{uid}/bus"
        if os.path.exists(dbus_path):
            env["DBUS_SESSION_BUS_ADDRESS"] = f"unix:path={dbus_path}"
    if not env.get("XDG_RUNTIME_DIR"):
        env["XDG_RUNTIME_DIR"] = f"/run/user/{uid}"

    try:
        subprocess.run(
            [
                "notify-send",
                "-u", "critical",
                "-i", "appointment-soon",
                "-a", "UTBK 2027 Assistant",
                title,
                body
            ],
            env=env,
            check=True
        )
        return True
    except Exception as e:
        print(f"Warning: notify-send failed ({e})", file=sys.stderr)
        return False

def install_cron():
    script_path = os.path.abspath(__file__)
    cron_lines = [
        f"# --- UTBK 2027 Daily Study Reminder ---",
        f"15 19 * * 1-4 python3 {script_path} >/dev/null 2>&1",
        f"45 19 * * 5 python3 {script_path} >/dev/null 2>&1",
        f"45 8 * * 6 python3 {script_path} >/dev/null 2>&1",
        f"45 14 * * 0 python3 {script_path} >/dev/null 2>&1",
        f"# ---------------------------------------"
    ]
    cron_block = "\n".join(cron_lines)

    try:
        current_crontab = subprocess.run(["crontab", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    except Exception:
        current_crontab = ""

    if "UTBK 2027 Daily Study Reminder" in current_crontab:
        print("Cron job UTBK 2027 sudah terpasang di crontab.")
        return True

    new_crontab = (current_crontab.strip() + "\n\n" + cron_block + "\n").lstrip()
    proc = subprocess.run(["crontab", "-"], input=new_crontab, text=True)
    if proc.returncode == 0:
        print("Cron job UTBK 2027 berhasil dipasang ke sistem crontab.")
        return True
    else:
        print("Gagal memasang cron job.")
        return False

def main():
    parser = argparse.ArgumentParser(description="UTBK 2027 Linux Desktop Reminder")
    parser.add_argument("--test", action="store_true", help="Trigger test notification now")
    parser.add_argument("--install-cron", action="store_true", help="Install automated crontab schedules")
    parser.add_argument("--dry-run", action="store_true", help="Print reminder without sending popup")
    args = parser.parse_args()

    if args.install_cron:
        install_cron()
        return

    today_info = get_today_reminder()
    if not today_info:
        print("Tidak ada jadwal belajar untuk hari ini.")
        return

    title = f"🔔 Persiapan Belajar UTBK ({today_info['subtes']})"
    body = f"⏰ Waktu: {today_info['time']}\n📚 Materi: {today_info['topic']}\n🎯 {today_info['target']}"

    send_notification(title, body, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

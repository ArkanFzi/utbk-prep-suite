import os
import sys
import argparse
import subprocess
from datetime import date
import urllib.request

sys.path.insert(0, "/home/arkan/Downloads")
from utbk_indicator_data import get_today_schedule

NTFY_TOPIC = "arkan_utbk_2027"

def send_checkin(target_date: date = None, dry_run: bool = False) -> bool:
    if target_date is None:
        target_date = date.today()

    sched = get_today_schedule(target_date)
    title = f"🔔 Evaluasi Selesai Belajar: {sched['subtes']}"
    body = (
        f"Waktu belajar 90 menit telah usai!\n"
        f"Materi: {sched['topic']}\n"
        f"Sudahkah kamu menyelesaikan sesi malam ini?\n"
        f"Ketik 'utbk-calendar done' di laptop untuk menandai selesai!"
    )

    print(f"[Check-in Notification]\nTitle: {title}\nBody:\n{body}")

    if dry_run:
        return True

    # 1. Desktop notification
    try:
        env = os.environ.copy()
        if not env.get("DISPLAY"):
            env["DISPLAY"] = ":1" if os.path.exists("/tmp/.X11-unix/X1") else ":0"
        if not env.get("DBUS_SESSION_BUS_ADDRESS"):
            uid = os.getuid()
            env["DBUS_SESSION_BUS_ADDRESS"] = f"unix:path=/run/user/{uid}/bus"

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
    except Exception as e:
        print(f"Warning: desktop notification failed: {e}", file=sys.stderr)

    # 2. Push to phone via ntfy.sh (No account or token required, instant push to ntfy app/browser)
    try:
        req = urllib.request.Request(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=body.encode("utf-8"),
            headers={
                "Title": title.encode("utf-8"),
                "Priority": "high",
                "Tags": "mortar_board,bell",
                "Actions": "view, Buka Kalender, https://calendar.google.com"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                print("Push notification sent to phone via ntfy.sh successfully.")
    except Exception as e:
        print(f"Warning: phone push notification failed: {e}", file=sys.stderr)

    return True

def install_cron():
    script_path = os.path.abspath(__file__)
    cron_line = f"0 21 * * * python3 {script_path} >/dev/null 2>&1"

    try:
        current_crontab = subprocess.run(["crontab", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    except Exception:
        current_crontab = ""

    if script_path in current_crontab:
        print("Check-in cron job sudah terpasang.")
        return True

    new_crontab = (current_crontab.strip() + f"\n\n# --- UTBK 21:00 Check-In Notification ---\n{cron_line}\n").lstrip()
    proc = subprocess.run(["crontab", "-"], input=new_crontab, text=True)
    if proc.returncode == 0:
        print("Cron job check-in 21:00 WIB berhasil dipasang.")
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="UTBK 2027 21:00 Check-in Evaluator")
    parser.add_argument("--dry-run", action="store_true", help="Print notification without sending")
    parser.add_argument("--install-cron", action="store_true", help="Install 21:00 daily check-in to crontab")
    args = parser.parse_args()

    if args.install_cron:
        install_cron()
        return

    send_checkin(dry_run=args.dry_run)

if __name__ == "__main__":
    main()

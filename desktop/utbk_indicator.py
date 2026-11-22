import os
import sys
import subprocess
import webbrowser
import fcntl
from datetime import date

import gi
gi.require_version('Gtk', '3.0')
try:
    gi.require_version('AyatanaAppIndicator3', '0.1')
    from gi.repository import AyatanaAppIndicator3 as appindicator
except ValueError:
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as appindicator

from gi.repository import Gtk, GLib

from utbk_indicator_data import (
    get_topbar_label,
    get_countdown_days,
    get_today_schedule,
    get_formula_of_the_day,
    EXAM_DATE
)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, CURRENT_DIR)

INDICATOR_ID = "utbk-2027-indicator"
LOCK_FILE = "/tmp/utbk_indicator.lock"
_lock_fd = None

def acquire_lock():
    global _lock_fd
    _lock_fd = open(LOCK_FILE, "w")
    try:
        fcntl.flock(_lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        print("Another instance of UTBK indicator is already running. Exiting.")
        sys.exit(0)

def open_url(url):
    webbrowser.open(url)

def open_file(path):
    subprocess.Popen(["xdg-open", path])

def launch_anki():
    subprocess.Popen(["anki"])

def launch_utbk_start():
    subprocess.Popen(["gnome-terminal", "--", "/home/arkan/.local/bin/utbk-start"])

def trigger_mobile_wallpaper():
    from utbk_mobile_hud import generate_wallpaper
    img_path = generate_wallpaper()
    subprocess.Popen(["xdg-open", img_path])

def trigger_usb_sync():
    script_path = os.path.join(PROJECT_ROOT, "scripts", "sync_phone_usb.sh")
    subprocess.Popen(["gnome-terminal", "--", script_path])

def open_web_dashboard():
    dist_index = os.path.join(PROJECT_ROOT, "web", "dist", "index.html")
    if os.path.exists(dist_index):
        subprocess.Popen(["xdg-open", dist_index])
    else:
        webbrowser.open("http://localhost:3000")

def trigger_checkin():
    from utbk_checkin_cron import send_checkin
    send_checkin()

def toggle_done(indicator):
    from utbk_calendar_cli import mark_session_done
    mark_session_done()
    update_indicator(indicator)

def toggle_focus_music():
    from utbk_music_focus import toggle_playback
    toggle_playback()

def quit_app(item):
    Gtk.main_quit()

def build_menu(indicator):
    menu = Gtk.Menu()

    today = date.today()
    days = get_countdown_days(today)
    sched = get_today_schedule(today)
    formula = get_formula_of_the_day(today)

    # 1. Header Target
    item_header = Gtk.MenuItem(label=f"🎯 UTBK 2027: H-{days} Menuju Ujian (21 April 2027)")
    item_header.set_sensitive(False)
    menu.append(item_header)

    item_prodi = Gtk.MenuItem(label="🏛️ Target: S1/D4 Informatika (ITS / UB / POLINEMA)")
    item_prodi.set_sensitive(False)
    menu.append(item_prodi)

    menu.append(Gtk.SeparatorMenuItem())

    # 2. Sesi Hari Ini
    item_sched_header = Gtk.MenuItem(label="📅 AGENDA BELAJAR HARI INI:")
    item_sched_header.set_sensitive(False)
    menu.append(item_sched_header)

    item_time = Gtk.MenuItem(label=f"   ⏰ Jam: {sched['time_str']}")
    item_time.set_sensitive(False)
    menu.append(item_time)

    item_subtes = Gtk.MenuItem(label=f"   📖 Subtes: {sched['subtes']}")
    item_subtes.set_sensitive(False)
    menu.append(item_subtes)

    # Truncate topic if too long
    topic_preview = sched['topic']
    if len(topic_preview) > 55:
        topic_preview = topic_preview[:52] + "..."
    item_topic = Gtk.MenuItem(label=f"   📝 Topik: {topic_preview}")
    item_topic.set_sensitive(False)
    menu.append(item_topic)

    menu.append(Gtk.SeparatorMenuItem())

    # 3. Formula of the day
    item_formula_hdr = Gtk.MenuItem(label=f"💡 FORMULA OF THE DAY ({formula['subtest']}):")
    item_formula_hdr.set_sensitive(False)
    menu.append(item_formula_hdr)

    # Truncate front & back
    q_preview = formula['front'].split('\n')[0]
    if len(q_preview) > 55:
        q_preview = q_preview[:52] + "..."
    item_q = Gtk.MenuItem(label=f"   ❓ {q_preview}")
    item_q.set_sensitive(False)
    menu.append(item_q)

    ans_preview = formula['back'].split('\n')[0]
    if len(ans_preview) > 55:
        ans_preview = ans_preview[:52] + "..."
    item_ans = Gtk.MenuItem(label=f"   👉 {ans_preview}")
    item_ans.set_sensitive(False)
    menu.append(item_ans)

    menu.append(Gtk.SeparatorMenuItem())

    # 4. Actions & Tools (Poin 2 & 3)
    item_ctrl_hdr = Gtk.MenuItem(label="⚡ KONTROL SESI & TOOLS:")
    item_ctrl_hdr.set_sensitive(False)
    menu.append(item_ctrl_hdr)

    item_start = Gtk.MenuItem(label="   🚀 Mulai Sesi Belajar (utbk-start 90m)")
    item_start.connect("activate", lambda _: launch_utbk_start())
    menu.append(item_start)

    item_done = Gtk.MenuItem(label="   ✅ Tandai Sesi Hari Ini Selesai [DONE]")
    item_done.connect("activate", lambda _: toggle_done(indicator))
    menu.append(item_done)

    item_mob_hud = Gtk.MenuItem(label="   📱 Render & Buka Wallpaper HP (1080x2400)")
    item_mob_hud.connect("activate", lambda _: trigger_mobile_wallpaper())
    menu.append(item_mob_hud)

    item_usb = Gtk.MenuItem(label="   📲 Sinkronisasi Data ke HP (USB ADB)")
    item_usb.connect("activate", lambda _: trigger_usb_sync())
    menu.append(item_usb)

    item_web = Gtk.MenuItem(label="   🌐 Buka Web Dashboard UTBK")
    item_web.connect("activate", lambda _: open_web_dashboard())
    menu.append(item_web)

    item_checkin = Gtk.MenuItem(label="   🔔 Kirim Notifikasi Check-In ke HP")
    item_checkin.connect("activate", lambda _: trigger_checkin())
    menu.append(item_checkin)

    from utbk_music_focus import get_playback_status
    status_music = get_playback_status()
    lbl_music = "   ⏸️ Jeda Musik Fokus (Spotify)" if status_music == "Playing" else "   🎵 Putar Musik Fokus (Spotify Lo-Fi/40Hz)"
    item_music = Gtk.MenuItem(label=lbl_music)
    item_music.connect("activate", lambda _: toggle_focus_music())
    menu.append(item_music)

    menu.append(Gtk.SeparatorMenuItem())

    # 5. External Shortcuts
    item_gcal = Gtk.MenuItem(label="🌐 Buka Google Calendar")
    item_gcal.connect("activate", lambda _: open_url("https://calendar.google.com"))
    menu.append(item_gcal)

    doc_error_log = os.path.join(PROJECT_ROOT, "docs", "template_error_log_utbk.md")
    item_error_log = Gtk.MenuItem(label="📝 Buka Template Error Log")
    item_error_log.connect("activate", lambda _: open_file(doc_error_log))
    menu.append(item_error_log)

    item_anki = Gtk.MenuItem(label="🧠 Buka Anki Desktop")
    item_anki.connect("activate", lambda _: launch_anki())
    menu.append(item_anki)

    item_refresh = Gtk.MenuItem(label="🔄 Refresh Indikator")
    item_refresh.connect("activate", lambda _: update_indicator(indicator))
    menu.append(item_refresh)

    menu.append(Gtk.SeparatorMenuItem())

    item_quit = Gtk.MenuItem(label="❌ Sembunyikan / Keluar")
    item_quit.connect("activate", quit_app)
    menu.append(item_quit)

    menu.show_all()
    return menu

def update_indicator(indicator):
    today = date.today()
    label = get_topbar_label(today)
    indicator.set_label(label, "UTBK 2027")
    indicator.set_menu(build_menu(indicator))
    return True # Keep GLib timer alive

def main():
    acquire_lock()
    indicator = appindicator.Indicator.new(
        INDICATOR_ID,
        "appointment-soon",
        appindicator.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    
    update_indicator(indicator)

    # Auto refresh every 60 seconds
    GLib.timeout_add_seconds(60, update_indicator, indicator)

    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

import os
import sys
from datetime import date
from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, CURRENT_DIR)
from utbk_indicator_data import (
    get_countdown_days,
    get_today_schedule,
    get_formula_of_the_day
)

OUTPUT_PATH = os.path.join(PROJECT_ROOT, "data", "utbk_mobile_lockscreen.png")

def get_font(size: int, bold: bool = False):
    font_candidates = [
        "/home/arkan/.local/share/fonts/Inter/Inter-Bold.ttf" if bold else "/home/arkan/.local/share/fonts/Inter/Inter-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in font_candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_card(draw, x, y, w, h, bg_color=(22, 26, 34), border_color=(44, 50, 64), radius=28):
    # Rounded card background
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=bg_color, outline=border_color, width=3)

def wrap_text(text: str, max_chars: int = 38):
    words = text.split()
    lines = []
    current_line = []
    for w in words:
        if len(' '.join(current_line + [w])) <= max_chars:
            current_line.append(w)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [w]
    if current_line:
        lines.append(' '.join(current_line))
    return lines

def generate_wallpaper(target_date: date = None) -> str:
    if target_date is None:
        target_date = date.today()

    width, height = 1080, 2400
    img = Image.new("RGB", (width, height), color=(11, 13, 17))
    draw = ImageDraw.Draw(img)

    # Decorative top glow accent
    draw.rectangle([0, 0, width, 12], fill=(220, 38, 38)) # Crimson accent bar

    # Header section
    font_sub = get_font(34, bold=True)
    font_uni = get_font(28, bold=False)
    draw.text((80, 260), "UTBK-SNBT 2027 TARGET INFORMATIKA", fill=(156, 163, 175), font=font_sub)
    draw.text((80, 310), "ITS (Institut Teknologi Sepuluh Nopember) • UB • POLINEMA", fill=(209, 213, 219), font=font_uni)

    # Big Countdown Card
    days = get_countdown_days(target_date)
    draw_card(draw, 80, 380, 920, 360, bg_color=(18, 22, 30), border_color=(220, 38, 38), radius=32)

    font_cd_label = get_font(36, bold=False)
    font_cd_val = get_font(128, bold=True)
    draw.text((120, 420), "COUNTDOWN MENUJU UJIAN (21 APRIL 2027)", fill=(156, 163, 175), font=font_cd_label)
    draw.text((120, 480), f"H-{days}", fill=(248, 113, 113), font=font_cd_val)
    draw.text((540, 560), "HARI LAGI", fill=(156, 163, 175), font=get_font(42, bold=True))
    draw.text((120, 650), "• Siswa SMK RPL • Peak Performance Preparation •", fill=(107, 114, 128), font=get_font(26))

    # Agenda Belajar Hari Ini Card
    sched = get_today_schedule(target_date)
    draw_card(draw, 80, 780, 920, 680, bg_color=(18, 22, 30), border_color=(59, 130, 246), radius=32)

    draw.text((120, 820), "AGENDA BELAJAR HARI INI", fill=(96, 165, 250), font=get_font(36, bold=True))
    draw.text((120, 870), f"Tanggal: {target_date.strftime('%A, %d %B %Y')}", fill=(156, 163, 175), font=get_font(28))

    draw.line([(120, 930), (920, 930)], fill=(37, 43, 56), width=2)

    # Subtest & Time
    draw.text((120, 960), "WAKTU", fill=(107, 114, 128), font=get_font(26, bold=True))
    draw.text((120, 1000), sched["time_str"], fill=(255, 255, 255), font=get_font(44, bold=True))

    draw.text((120, 1080), "SUBTES UTAMA", fill=(107, 114, 128), font=get_font(26, bold=True))
    draw.text((120, 1120), sched["subtes"], fill=(52, 211, 153), font=get_font(42, bold=True))

    draw.text((120, 1200), "MATERI FOKUS", fill=(107, 114, 128), font=get_font(26, bold=True))
    topic_lines = wrap_text(sched["topic"], max_chars=34)
    ty = 1240
    for line in topic_lines[:2]:
        draw.text((120, ty), line, fill=(229, 231, 235), font=get_font(34, bold=False))
        ty += 46

    draw.text((120, 1370), f"Target: {sched['target']}", fill=(156, 163, 175), font=get_font(26))

    # Formula of the Day Card
    formula = get_formula_of_the_day(target_date)
    draw_card(draw, 80, 1500, 920, 680, bg_color=(18, 22, 30), border_color=(234, 179, 8), radius=32)

    draw.text((120, 1540), f"FORMULA OF THE DAY ({formula['subtest']})", fill=(250, 204, 21), font=get_font(36, bold=True))
    draw.line([(120, 1600), (920, 1600)], fill=(37, 43, 56), width=2)

    draw.text((120, 1630), "PERTANYAAN / KONSEP:", fill=(107, 114, 128), font=get_font(26, bold=True))
    q_lines = wrap_text(formula["front"], max_chars=34)
    qy = 1670
    for line in q_lines[:3]:
        draw.text((120, qy), line, fill=(255, 255, 255), font=get_font(34, bold=True))
        qy += 48

    draw.text((120, 1850), "RUMUS / TRIK CEPAT:", fill=(107, 114, 128), font=get_font(26, bold=True))
    a_lines = wrap_text(formula["back"], max_chars=34)
    ay = 1890
    for line in a_lines[:4]:
        draw.text((120, ay), line, fill=(74, 222, 128), font=get_font(34, bold=False))
        ay += 46

    # Bottom footer motivation
    draw.text((80, 2240), "CONSISTENCY BEATS TALENT • UTBK SNBT 2027", fill=(75, 85, 99), font=get_font(28, bold=True))
    draw.text((80, 2280), "Terintegrasi: Google Calendar • Anki FSRS • GNOME Indicator", fill=(55, 65, 81), font=get_font(24))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    img.save(OUTPUT_PATH, "PNG")
    print(f"Wallpaper generated: {OUTPUT_PATH}")
    return OUTPUT_PATH

if __name__ == "__main__":
    generate_wallpaper()

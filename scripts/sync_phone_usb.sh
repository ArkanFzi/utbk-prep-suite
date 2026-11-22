#!/usr/bin/env bash
# ==============================================================================
# sync_phone_usb.sh: Direct USB ADB Synchronization to Xiaomi Redmi 9A
# ==============================================================================
set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="${PROJECT_ROOT}/data"

echo -e "\033[1;36m====================================================\033[0m"
echo -e " 📱 \033[1mUTBK 2027: DIRECT USB SYNC TO SMARTPHONE (ADB)\033[0m"
echo -e "\033[1;36m====================================================\033[0m"

# 1. Check ADB availability
if ! command -v adb >/dev/null 2>&1; then
    # Check fallback path in Downloads if not in PATH
    if [ -x "/home/arkan/Downloads/scrcpy-linux-x86_64-v5.0.1/adb" ]; then
        export PATH="/home/arkan/Downloads/scrcpy-linux-x86_64-v5.0.1:$PATH"
    else
        echo -e "\033[91m[ERROR]\033[0m adb tidak ditemukan di sistem."
        exit 1
    fi
fi

# 2. Check connected devices
DEVICE_COUNT=$(adb devices | grep -v "List" | grep -v "^$" | grep "device$" | wc -l)
if [ "$DEVICE_COUNT" -eq 0 ]; then
    echo -e "\033[91m[ERROR]\033[0m Tidak ada HP yang terhubung atau belum diotorisasi USB Debugging."
    echo -e "Pastikan kabel USB terpasang dan layar HP tidak terkunci (izinkan dialog debugging)."
    exit 1
fi

DEVICE_NAME=$(adb devices -l | grep "device usb:" | awk '{print $4, $5}')
echo -e "\033[1;32m[OK]\033[0m Perangkat terhubung: \033[1m${DEVICE_NAME}\033[0m"

# 3. Create destination folders on device
echo -e "\n📂 Menyiapkan folder tujuan di HP..."
adb shell "mkdir -p /sdcard/Pictures/UTBK /sdcard/Download/UTBK"

# 4. Push Mobile Lockscreen HUD
LOCKSCREEN_IMG="${DATA_DIR}/utbk_mobile_lockscreen.png"
if [ -f "$LOCKSCREEN_IMG" ]; then
    echo -e "🖼️  Mengirim Wallpaper Lockscreen HUD..."
    adb push "$LOCKSCREEN_IMG" "/sdcard/Pictures/UTBK/utbk_mobile_lockscreen.png" >/dev/null
    # Trigger MediaScanner so it appears immediately in MIUI Gallery
    adb shell "am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/UTBK/utbk_mobile_lockscreen.png" >/dev/null
    echo -e "   \033[92m✓\033[0m Tersimpan di: /sdcard/Pictures/UTBK/utbk_mobile_lockscreen.png (Muncul di Galeri)"
else
    echo -e "   \033[93m⚠\033[0m File lockscreen belum digenerate."
fi

# 5. Push Calendar ICS
ICS_FILE="${DATA_DIR}/jadwal_utbk_2027.ics"
if [ -f "$ICS_FILE" ]; then
    echo -e "📅 Mengirim Jadwal Kalender (.ics)..."
    adb push "$ICS_FILE" "/sdcard/Download/UTBK/jadwal_utbk_2027.ics" >/dev/null
    echo -e "   \033[92m✓\033[0m Tersimpan di: /sdcard/Download/UTBK/jadwal_utbk_2027.ics"
fi

# 6. Push Anki Flashcard Starter Deck
ANKI_CSV="${DATA_DIR}/anki_utbk2027_starter.csv"
if [ -f "$ANKI_CSV" ]; then
    echo -e "🧠 Mengirim Starter Deck Flashcard Anki (.csv)..."
    adb push "$ANKI_CSV" "/sdcard/Download/UTBK/anki_utbk2027_starter.csv" >/dev/null
    echo -e "   \033[92m✓\033[0m Tersimpan di: /sdcard/Download/UTBK/anki_utbk2027_starter.csv"
fi

# 7. Check AnkiDroid installation
if adb shell "pm list packages | grep -q com.ichi2.anki"; then
    echo -e "\n🎯 \033[1;32mAnkiDroid terdeteksi di HP!\033[0m"
    echo -e "   Buka AnkiDroid -> Menu (titik 3) -> Kelola Koleksi -> Impor -> Pilih file di Download/UTBK/"
fi

echo -e "\n\033[1;32m====================================================\033[0m"
echo -e " ✨ \033[1mSINKRONISASI USB SELESAI!\033[0m Seluruh aset belajar siap di HP."
echo -e "\033[1;32m====================================================\033[0m"

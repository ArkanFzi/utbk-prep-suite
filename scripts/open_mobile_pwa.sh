#!/usr/bin/env bash
# ==============================================================================
# open_mobile_pwa.sh: Launch Live PWA on Connected Android Device (Redmi 9A)
# ==============================================================================
set -e

# Target live URL (GitHub Pages / GCP)
APP_URL="${1:-https://arkanfzi.github.io/utbk-prep-suite/}"

echo -e "\033[1;36m====================================================\033[0m"
echo -e " 🚀 \033[1mLAUNCHING LIVE UTBK PWA ON REDMI 9A\033[0m"
echo -e "\033[1;36m====================================================\033[0m"

# 1. Check ADB
if ! command -v adb >/dev/null 2>&1; then
    if [ -x "/home/arkan/Downloads/scrcpy-linux-x86_64-v5.0.1/adb" ]; then
        export PATH="/home/arkan/Downloads/scrcpy-linux-x86_64-v5.0.1:$PATH"
    else
        echo -e "\033[91m[ERROR]\033[0m ADB tidak ditemukan."
        exit 1
    fi
fi

# 2. Check Device
if ! adb get-state 1>/dev/null 2>&1; then
    echo -e "\033[91m[ERROR]\033[0m Perangkat HP tidak terdeteksi via USB ADB."
    exit 1
fi

echo -e "🌐 Membuka URL: \033[1;32m${APP_URL}\033[0m di Chrome HP..."
adb shell "am start -a android.intent.action.VIEW -d '${APP_URL}'" >/dev/null

echo -e "\n\033[1;32m[SUKSES]\033[0m Aplikasi telah dibuka di layar HP!"
echo -e "💡 \033[1mPetunjuk PWA:\033[0m Klik menu Chrome (titik tiga) -> Pilih 'Tambahkan ke Layar Utama' / 'Install App'."

#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import argparse

MPRIS_DEST = "org.mpris.MediaPlayer2.spotify"
MPRIS_PATH = "/org/mpris/MediaPlayer2"
MPRIS_PLAYER = "org.mpris.MediaPlayer2.Player"

DEFAULT_FOCUS_URI = "spotify:playlist:37i9dQZF1DXdLEN7aqioXM" # Brain Food / Deep Focus

def is_spotify_running() -> bool:
    try:
        res = subprocess.run(
            ["busctl", "--user", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        return MPRIS_DEST in res.stdout
    except Exception:
        return False

def launch_spotify():
    if not is_spotify_running():
        subprocess.Popen(["spotify"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(10):
            time.sleep(0.5)
            if is_spotify_running():
                break

def get_playback_status() -> str:
    if not is_spotify_running():
        return "Offline"
    try:
        res = subprocess.run(
            ["busctl", "--user", "get-property", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "PlaybackStatus"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        if res.returncode == 0:
            # Output format: s "Playing" or s "Paused"
            parts = res.stdout.strip().split('"')
            if len(parts) >= 2:
                return parts[1]
    except Exception:
        pass
    return "Unknown"

def set_volume(volume: float = 0.40) -> bool:
    # Volume is between 0.0 and 1.0
    vol = max(0.0, min(1.0, float(volume)))
    try:
        res = subprocess.run(
            ["busctl", "--user", "set-property", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "Volume", "d", str(vol)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        return res.returncode == 0
    except Exception:
        return False

def play_focus(uri: str = None) -> bool:
    target_uri = uri or DEFAULT_FOCUS_URI
    if not is_spotify_running():
        launch_spotify()

    try:
        # First set comfortable study volume
        set_volume(0.40)
        # Open focus playlist
        res = subprocess.run(
            ["busctl", "--user", "call", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "OpenUri", "s", target_uri],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=3
        )
        if res.returncode != 0:
            # Fallback to simple Play
            subprocess.run(
                ["busctl", "--user", "call", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "Play"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=2
            )
        return True
    except Exception as e:
        print(f"Error starting music: {e}", file=sys.stderr)
        return False

def pause() -> bool:
    if not is_spotify_running():
        return True
    try:
        res = subprocess.run(
            ["busctl", "--user", "call", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "Pause"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        return res.returncode == 0
    except Exception:
        return False

def toggle_playback() -> bool:
    if not is_spotify_running():
        launch_spotify()
        return play_focus()

    try:
        res = subprocess.run(
            ["busctl", "--user", "call", MPRIS_DEST, MPRIS_PATH, MPRIS_PLAYER, "PlayPause"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        return res.returncode == 0
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description="UTBK 2027 Spotify Focus Music Controller")
    parser.add_argument("--play", action="store_true", help="Start focus playlist")
    parser.add_argument("--pause", action="store_true", help="Pause music")
    parser.add_argument("--toggle", action="store_true", help="Toggle play/pause")
    parser.add_argument("--status", action="store_true", help="Show playback status")
    parser.add_argument("--volume", type=float, help="Set volume (0.0 - 1.0)")
    args = parser.parse_args()

    if args.play:
        success = play_focus()
        print(f"Play focus music: {'Success' if success else 'Failed'}")
    elif args.pause:
        success = pause()
        print(f"Pause music: {'Success' if success else 'Failed'}")
    elif args.toggle:
        success = toggle_playback()
        print(f"Toggle music: {'Success' if success else 'Failed'}")
    elif args.volume is not None:
        success = set_volume(args.volume)
        print(f"Set volume {args.volume}: {'Success' if success else 'Failed'}")
    elif args.status:
        print(f"Spotify Status: {get_playback_status()}")
    else:
        print(f"Spotify Status: {get_playback_status()}")

if __name__ == "__main__":
    main()

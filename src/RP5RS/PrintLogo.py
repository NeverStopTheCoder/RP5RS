
import sys
import time
import random
import os

# 1. BOLD Color & Style Definitions
R = "\033[1;31m"          # Bold Red
O = "\033[1;38;5;208m"    # Bold Orange
Y = "\033[1;33m"          # Bold Yellow
G = "\033[1;32m"          # Bold Green
B = "\033[1;34m"          # Bold Blue
RESET = "\033[0m"         # Reset back to normal white
DIM = "\033[2m"           # Faint text modifier

# 2. The Synchronized Logo Layout List
logo_lines = [
    "··································································\n",
    f":{R}88888888ba   {O}88888888ba   {Y}8888888888   {G}88888888ba    {B}ad88888ba  {RESET}:\n",
    f":{R}88      \"8b  {O}88      \"8b  {Y}88           {G}88      \"8b  {B}d8\"     \"8b {RESET}:\n",
    f":{R}88      ,8P  {O}88      ,8P  {Y}88  ____     {G}88      ,8P  {B}Y8,         {RESET}:\n",
    f":{R}88aaaaaa8P'  {O}88aaaaaa8P'  {Y}88a8PPPP8b,  {G}88aaaaaa8P'  {B}`Y8aaaaa,   {RESET}:\n",
    f":{R}88\"\"\"\"88'    {O}88\"\"\"\"\"\"'    {Y}PP\"      `8b {G}88\"\"\"\"88'      {B}`\"\"\"\"\"8b, {RESET}:\n",
    f":{R}88    `8b    {O}88                      {Y}d8  {G}88    `8b            {B}`8b {RESET}:\n",
    f":{R}88     `8b   {O}88               {Y}Y8a     a8P  {G}88     `8b   {B}Y8a     a8P {RESET}:\n",
    f":{R}88      `8b  {O}88                {Y}\"Y88888P\"   {G}88      `8b   {B}\"Y88888P\"  {RESET}:\n",
    "··································································\n"
]

# 3. Handle Shuffle Bag Memory Files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYLIST_FILE = os.path.join(SCRIPT_DIR, ".boot_playlist")
LAST_STYLE_FILE = os.path.join(SCRIPT_DIR, ".last_played_style")

playlist = []
just_played = -1

if os.path.exists(PLAYLIST_FILE):
    try:
        with open(PLAYLIST_FILE, "r") as f:
            data = f.read().strip()
            if data:
                playlist = [int(x) for x in data.split(",")]
    except:
        playlist = []

if os.path.exists(LAST_STYLE_FILE):
    try:
        with open(LAST_STYLE_FILE, "r") as f:
            just_played = int(f.read().strip())
    except:
        just_played = -1

# If all animations have played, reset the deck and verify no boundary duplicates
if not playlist:
    new_deck = [0, 1, 2, 3]
    random.shuffle(new_deck)
    while new_deck[0] == just_played:
        random.shuffle(new_deck)
    playlist = new_deck

boot_style = playlist.pop(0)

with open(PLAYLIST_FILE, "w") as f:
    f.write(",".join(map(str, playlist)))

with open(LAST_STYLE_FILE, "w") as f:
    f.write(str(boot_style))

# Clear screen completely
sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()

# === STYLE 0: DROP DOWN FROM TOP ===
if boot_style == 0:
    for line in logo_lines:
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.12)

# === STYLE 1: RISE UP FROM BOTTOM ===
elif boot_style == 1:
    sys.stdout.write("\n" * 25)
    sys.stdout.flush()
    for line in logo_lines:
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.15)

# === STYLE 2: WIPE IN FROM LEFT ===
elif boot_style == 2:
    for line in logo_lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char not in ['\033', '[', 'm', ';', '1', '3', '2', '0', '8', '5', '4']:
                time.sleep(0.002)
        time.sleep(0.04)

# === STYLE 3: SLIDE IN FROM THE RIGHT ===
elif boot_style == 3:
    clean_lines = [line.rstrip('\n') for line in logo_lines]
    for width in range(60, -1, -4):
        sys.stdout.write("\033[H")
        for line in clean_lines:
            sys.stdout.write(" " * width + line + "\033[K\n")
        sys.stdout.flush()
        time.sleep(0.04)

# 5. Clean Credit Reveal & Loading Text
time.sleep(0.4)
print(f"{DIM}                  Made By NeverStopTheCoder © 2026{RESET}")
print("LOADING...\n")

#!/bin/bash
sudo mkdir /sd

echo "[Target]
Hardware=rpi

[Input]
SCAN_CODES=/dev/input/event0
BTN_LEFT=105
BTN_RIGHT=106
BTN_UP=103
BTN_DOWN=108
BTN_A=57
BTN_B=29
BTN_MENU=41
BTN_RESET=14
kbd_mode=1" | sudo tee /sd/arcade.cfg

# 2. Apply the Pi 5 signature spoofing trick
sudo umount -l /proc/cpuinfo 2>/dev/null
sudo rm -f /tmp/cpuinfo
cp /proc/cpuinfo /tmp/cpuinfo
sudo sh -c 'echo "Hardware : BCM2835" >> /tmp/cpuinfo'
sudo mount --bind /tmp/cpuinfo /proc/cpuinfo

# 1. Force terminal screen blanking off cleanly
sudo TERM=linux sh -c 'setterm -blank 0 -powerdown 0 > /dev/tty1' 2>/dev/null

# 2. Print your custom boot logo directly to the screen
cat << 'EOF'

··································································
:88888888ba   88888888ba   8888888888   88888888ba    ad88888ba  :
:88      "8b  88      "8b  88           88      "8b  d8"     "8b :
:88      ,8P  88      ,8P  88  ____     88      ,8P  Y8,         :
:88aaaaaa8P'  88aaaaaa8P'  88a8PPPP8b,  88aaaaaa8P'  `Y8aaaaa,   :
:88""""88'    88""""""'    PP"      `8b  88""""88'      `"""""8b, :
:88    `8b    88                     d8  88    `8b            `8b :
:88     `8b   88               Y8a     a8P  88     `8b   Y8a     a8P :
:88      `8b  88                "Y88888P"   88      `8b   "Y88888P"  :
··································································

Made By NeverStopTheCoder © 2026
LOADING...
EOF

# 3. Wait 2 seconds for the player to see your logo
sleep 2

# 4. The Crash-Proof Game Loop
while true; do
    echo "Starting Game Match..."
    
    # Bash automatically finds and targets any execution-ready game file using ./*.elf
    sudo chmod +x ./*.elf 2>/dev/null
    sudo SDL_VIDEODRIVER=kmsdrm SDL_AUDIODRIVER=alsa ./*.elf --hw rpi
    
    echo "Match concluded. Deep cleaning memory cache..."
    sync
    sleep 1.5
    echo "Ready for next match!"
done

#!/bin/bash
sudo mkdir /sd
sudo chmod +x ./*.elf 2>/dev/null

trap 'sudo pkill -9 -f "tennis.elf" 2>/dev/null; exit' INT TERM EXIT

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
python3 "$(dirname "$0")/PrintLogo.py"

# 3. Wait 2 seconds for the player to see your logo
sleep 2

# 4. The Crash-Proof Game Loop
while true; do
    echo "Starting Game Match..."
    
    sudo SDL_VIDEODRIVER=kmsdrm SDL_AUDIODRIVER=oss ./*.elf --hw rpi >/dev/null 2>&1 &
    PID=$!
    wait $PID 2>/dev/null
    
    echo "Match concluded. Deep cleaning memory cache..."
    sync
    sleep 1.5
    echo "Ready for next match!"
done

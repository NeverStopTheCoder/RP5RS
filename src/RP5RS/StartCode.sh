
sudo mkdir /sd

echo "[Target]
Hardware=pc

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

echo "#!/bin/bash

sudo umount -l /proc/cpuinfo
sudo rm -f /tmp/cpuinfo

cp /proc/cpuinfo /tmp/cpuinfo
sudo sh -c 'echo "Hardware : BCM2835" >> /tmp/cpuinfo'
sudo mount --bind /tmp/cpuinfo /proc/cpuinfo

sudo SDL_VIDEODRIVER=kmsdrm SDL_EVDEV_DEVICES=/dev/input/event0 ./*.elf --hw rpi" | sudo tee myGame.sh

cat << 'EOF' > converter.py
import os,glob,time

def print_boot_logo():
    # The 'r' before the quotes tells Python: "Treat every single character as pure art"
    logo = r"""
··································································
:88888888ba   88888888ba   8888888888   88888888ba    ad88888ba  :
:88      "8b  88      "8b  88           88      "8b  d8"     "8b :
:88      ,8P  88      ,8P  88  ____     88      ,8P  Y8,         :
:88aaaaaa8P'  88aaaaaa8P'  88a8PPPP8b,  88aaaaaa8P'  `Y8aaaaa,   :
:88""""88'    88""""""'    PP"     `8b  88""""88'      `"""""8b, :
:88    `8b    88                    d8  88    `8b            `8b :
:88     `8b   88           Y8a     a8P  88     `8b   Y8a     a8P :
:88      `8b  88            "Y88888P"   88      `8b   "Y88888P"  :
··································································
    """
    print(logo)
    print("Made By NeverStopTheCoder © 2026")
    time.sleep(2)
    
def setup_cartridge():

    #1. Find the game file (any .elf)

    elf_files = glob.glob("*.elf")
    if not elf_files:
        print("Error: No game (.elf) found on this cartridge!")
        return
    game_name = elf_files[0]
    print(f"Preparing cartridge for: {game_name}")

    # 2. Force permissions
    os.system(f"chmod +x {game_name}")

    # 3. Create the boot script (The Bridge)
    with open("boot.sh", "w") as f:
        f.write(f"#!/bin/bash\n")
        f.write(f"sleep 2\n") # Wait for Pi 5 graphics to wake up
        f.write(f"sudo ./{game_name} --hw rpi \n")

    os.system("chmod +x boot.sh")
    print("LOADING...")
    time.sleep(0.5)
    print("Cartridge is ready for Auto-Boot!")
print_boot_logo()
setup_cartridge()
EOF

python3 converter.py

sudo chmod +x myGame.sh
sudo chmod +x ./*.elf

sudo ./myGame.sh

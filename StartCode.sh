
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

sudo SDL_VIDEODRIVER=kmsdrm SDL_EVDEV_DEVICES=/dev/input/event0 ./arcade-myGame.elf --hw rpi" | sudo tee myGame.sh

echo "import os,import glob

def setup_cartridge():

#1. Find the game file (any .elf)

elf_files = glob.glob("*.elf")if not elf_files:print("Error: No game (.elf) found on this cartridge!")return
game_name = elf_files[0]
print(f"Preparing cartridge for: {game_name}")

# 2. Force permissions
os.system(f"chmod +x {game_name}")

# 3. Create the boot script (The Bridge)
with open("boot.sh", "w") as f:
    f.write(f"#!/bin/bash\n")
    f.write(f"sleep 2\n") # Wait for Pi 5 graphics to wake up
    f.write(f"sudo ./{game_name} --hw rpi\n")

os.system("chmod +x boot.sh")
print("Cartridge is ready for Auto-Boot!")

setup_cartridge()" | sudo tee converter.py

python3 converter.py

chmod +x myGame.sh

chmod +x arcade-myGame.elf

./myGame.sh

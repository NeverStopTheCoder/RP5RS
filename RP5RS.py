import os
import glob

# This keeps track of the game name between functions
CURRENT_GAME = ""

def SetCurrentGameTo(game_name=None):
    global CURRENT_GAME
    # If no name is given, automatically grab the first .elf file
    if game_name is None:
        elf_files = glob.glob("*.elf")
        if not elf_files:
            print("Error: No game (.elf) found in this directory!")
            return False
        CURRENT_GAME = elf_files[0]
    else:
        CURRENT_GAME = game_name
        
    print(f"Current game target set to: {CURRENT_GAME}")
    return True

def RunGame():
    global CURRENT_GAME
    # Safety check: if they didn't run SetCurrentGameTo first, run it now
    if not CURRENT_GAME:
        if not SetCurrentGameTo():
            return
            
    print(f"Launching your custom setup script for {CURRENT_GAME}...")
    
    # Make sure your shell script has execution permissions
    os.system("chmod +x StartCode.sh")
    
    # Run your exact shell script exactly as you wrote it
    os.system("sudo ./StartCode.sh")

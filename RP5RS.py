
def RunGame():
    global CURRENT_GAME
    # Fallback safety check in case they didn't run SetCurrentGameTo first
    if not CURRENT_GAME:
        if not SetCurrentGameTo():
            return
CURRENT_GAME = ""

def SetCurrentGameTo(game_name=None):
    global CURRENT_GAME
    # If no name is given, auto-detect the first .elf file in the folder
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
    

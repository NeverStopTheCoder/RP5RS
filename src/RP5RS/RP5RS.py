import os
import glob
import paramiko 
from pathlib import Path

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
    
    package_dir = os.path.dirname(os.path.abspath(__file__))
    start_code_path = os.path.join(package_dir, "StartCode.sh")

    os.system(f"chmod +x {start_code_path}")
    os.system(f"sudo {start_code_path}")
""" 
def SendGameOver(PI_id,Username,Password,game_name=None,ReplaceOldFiles=False,SetAsCurrent=False,LaunchGame=False):
    global CURRENT_GAME
    if SetAsCurrent is True:
        SetCurrentGameTO()
    if ReplaceOldFiles is True:
        home_dir = Path.home()
        os.rename(home_dir/game_name,home_dir/"UsedGame.elf")
        game_name = "UsedGame.elf"
        elf_files = glob.glob(f"{home_dir}/*.elf")
        for file in elf_files: 
            if file != f"{home_dir}/UsedGame.elf":
                os.remove(file)
    ssh = paramiko.SSHClient() 
    ssh.connect(PI_id, username=Username, password=Password) # Default IP/login, this may be different for you
    sftp = ssh.open_sftp()
    # Localpath is a string containing the path of the local file, remotepath is where the file should be copied on the raspberry pi
    sftp.put(home_dir/game_name, f'/home/{Username}/{game_name}')
    if LaunchGame is True:
    ssh.exec_command(f"python3 /home/{Username}/RunGame.py")
    sftp.close()
    ssh.close()
    if SetAsCurrent is True:
        CURRENT_GAME = game_name
"""
def SendGameOver(PI_id, Username, Password, game_name=None, ReplaceOldFiles=False, SetAsCurrent=False, LaunchGame=False):
    global CURRENT_GAME
    # 1. Defined at the top so it's always ready for the SFTP transfer
    home_dir = Path.home()   
    # 2. Fixed the function name typo
    if SetAsCurrent is True:
        SetCurrentGameTo()       
    # 3. Local file cleanup (Only runs if ReplaceOldFiles is True)
    if ReplaceOldFiles is True:
        os.rename(home_dir/game_name, home_dir/"UsedGame.elf")
        game_name = "UsedGame.elf"
        elf_files = glob.glob(f"{home_dir}/*.elf")
        for file in elf_files: 
            if file != f"{home_dir}/UsedGame.elf":
                os.remove(file)              
    # 4. Network block (Runs EVERY time now, outside the file cleanup block)
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Bypasses the known_hosts wall
    ssh.connect(PI_id, username=Username, password=Password) 
    sftp = ssh.open_sftp()
    sftp.put(home_dir/game_name, f'/home/{Username}/{game_name}')
    sftp.close() 
    # 5. Fixed the indentation so the game only launches if requested
    if LaunchGame is True:
        ssh.exec_command(f"python3 /home/{Username}/RunGame.py")  
    ssh.close()
    if SetAsCurrent is True:
        CURRENT_GAME = game_name
        
def ReplaceAllFilesWith(game_name=None):
        home_dir = Path.home()
        os.rename(home_dir/game_name,home_dir/"UsedGame.elf")
        game_name = "UsedGame.elf"
        elf_files = glob.glob(f"{home_dir}/*.elf")
        for file in elf_files: 
            if file != f"{home_dir}/UsedGame.elf":
                os.remove(file)
                return "UsedGame.elf"

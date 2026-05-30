# RP5RS
Automated initialization environment wrapper for MakeCode Arcade on the Raspberry Pi 5.
/python module to easily run a makecode arcade game
## How to run:
```python
import RP5RS
RP5RS.SetCurrentGameTo()
RP5RS.RunGame()
```
You can put a elf file in the SetCurrentGameTo() function like this
```python
RP5RS.SetCurrentGameTo(myGame.elf)
```
But if you dont put a file in there it will grab the first one from the home folder

Note:this only works for a keyboard right now also make sure for right now you plug in the keyboard first or it wont work right

## Logo At Boot Up
```
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
Made By NeverStopTheCoder © 2026
LOADING...
Cartridge is ready for Auto-Boot!
(game runs)
```
## More Code
```python
# Sends the game over to the pi from the linux folder on your device (use this on the sender not the pi)
SendGameOver()
# Replaces all the files in the home folder with the set Game
ReplaceAllFilesWith()
```

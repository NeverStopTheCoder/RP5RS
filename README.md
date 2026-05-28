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

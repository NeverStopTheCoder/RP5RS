# Pull the functions from your sub-file straight to the surface
from .RP5RS import SetCurrentGameTo, RunGame, SendGameOver, ReplaceAllFilesWith

# (Optional) This tells Python exactly what is allowed to be exported
__all__ = ['SetCurrentGameTo', 'RunGame', 'SendGameOver', 'ReplaceAllFilesWith']

from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager

class Walltroll(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.wall, SpriteManager.wall_sprite, team, position)
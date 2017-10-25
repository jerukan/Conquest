from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager

class ArcherUnit(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.archer, SpriteManager.archer_sprite, team, position)
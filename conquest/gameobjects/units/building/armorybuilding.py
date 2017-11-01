from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager


class ArmoryBuilding(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.armory, SpriteManager.armory_sprite, team, position)
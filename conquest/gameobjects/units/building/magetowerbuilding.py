from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager


class MagetowerBuilding(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.magetower, SpriteManager.magetower_sprite, team, position)

    def onCreation(self):
        pass
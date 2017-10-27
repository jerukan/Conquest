from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager


class FarmBuilding(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.farm, SpriteManager.farm_sprite, team, position)


    def onCreation(self):
        self.team.maxUnits += 3


    def onDeath(self):
        self.team.maxUnits -= 3
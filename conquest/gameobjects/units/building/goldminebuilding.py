from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.constants import Constants
from util.spritemanager import SpriteManager

class GoldmineBuilding(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.goldmine, SpriteManager.goldmine_sprite, team, position)


    def onCreation(self):
        self.team.moneyProduction += Constants.GOLDMINE_PRODUCTION


    def onDeath(self):
        self.team.moneyProduction -= Constants.GOLDMINE_PRODUCTION
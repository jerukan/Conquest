import copy

from gameobjects.units.gameunit import UnitType
from util.constants import Constants


class Player:
    """
    Contains stats and everything needed for a player of the game
    ree ree ree
    """

    def __init__(self, num, color, aiControlled = False):
        self.number = num
        self.color = color
        self.aiControlled = aiControlled

        '''pretty cool stuff i guess'''
        self.unitlist = []
        self.soldierlist = []
        self.buildinglist = []

        self.money = Constants.DEFAULT_STARTING_MONEY
        self.moneyProduction = Constants.DEFAULT_MONEY_PRODUCTION
        self.maxUnits = Constants.DEFAULT_MAX_UNITS


    def updateUnitlist(self, units):
        templist = []
        for unit in units:
            if unit.team == self:
                templist.append(unit)

        self.unitlist = templist
        self.soldierlist = self.getSoldiers()
        self.buildinglist = self.getBuildings()


    def getSoldiers(self):
        templist = []
        for unit in self.unitlist:
            if unit.unittype == UnitType.SOLDIER:
                templist.append(unit)
        return templist


    def getBuildings(self):
        templist = []
        for unit in self.unitlist:
            if unit.unittype == UnitType.BUILDING:
                templist.append(unit)
        return templist


    def produceMoney(self):
        self.money += self.moneyProduction


    def deductMoney(self, value):
        if not self.money - value < 0:
            self.money -= value


    def addMoney(self, value):
        self.money += value
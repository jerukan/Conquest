from gameobjects.units import *
from gameobjects.units.gameunit import UnitType
from gameobjects.units.unit_info import UnitInfo


class UnitList:

    """
    List of all units and their corresponding classes
    Organized in cool ways
    """
    allUnits = {
        "spearman": SpearmanUnit,
        "footman": FootmanUnit,
        "archer": ArcherUnit,
        "village": VillageBuilding,
        "gold mine": GoldmineBuilding,
        "wall": Walltroll,
        "farm": FarmBuilding
    }

    # sorts all the unorganized shit into more organized shit
    soldiers = []
    buildings = []
    buildableSoldiers = []
    buildableBuildings = []

    def initLists(self):
        for unit in self.allUnits:
            if UnitInfo.allUnitInfo[unit]["type"] == UnitType.SOLDIER:
                self.soldiers.append(unit)
                if UnitInfo.allUnitInfo[unit]["buildable"]:
                    self.buildableSoldiers.append(unit)
            if UnitInfo.allUnitInfo[unit]["type"] == UnitType.BUILDING:
                self.soldiers.append(unit)
                if UnitInfo.allUnitInfo[unit]["buildable"]:
                    self.buildableBuildings.append(unit)
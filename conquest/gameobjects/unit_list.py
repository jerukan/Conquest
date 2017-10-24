from gameobjects.units import *

class UnitList:

    """
    List of all BUILDABLE units
    So no villages
    """

    soldierList = {
        "spearman": SpearmanUnit,
        "footman": FootmanUnit,
        "archer": ArcherUnit
    }
    buildingList = {
        "gold mine": GoldmineBuilding,
        "wall": Walltroll
    }
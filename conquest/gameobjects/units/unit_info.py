from gameobjects.units.gameunit import UnitType
from util.constants import Constants


class UnitInfo:
    """
    A class documenting all the stats of the units
    Stats are om the following order: [maxhealth, attack, speed, availableattacks, range, cost]
    """
    # SOLDIER UNITS
    spearman = {
        "name": "spearman",
        "type": UnitType.SOLDIER,
        "stats": [2, 2, 3, 1, 1, 2],
        "requiredunit": "armory",
        "buildable": True,
        "description": "Completely broken"
    }
    footman = {
        "name": "footman",
        "type": UnitType.SOLDIER,
        "stats": [2, 1, 2, 1, 1, 1],
        "requiredunit": None,
        "buildable": True,
        "description": "Ole reliable"
    }
    archer = {
        "name": "archer",
        "type": UnitType.SOLDIER,
        "stats": [1, 1, 2, 1, 2, 1],
        "requiredunit": None,
        "buildable": True,
        "description": "RUSH RUSH RUSH"
    }
    # BUILDING UNITS
    village = {
        "name": "village",
        "type": UnitType.BUILDING,
        "stats": [6, 0, 0, 0, 0, 0],
        "requiredunit": None,
        "buildable": False,
        "description": "Don\'t let this die"
    }
    goldmine = {
        "name": "gold mine",
        "type": UnitType.BUILDING,
        "stats": [3, 0, 0, 0, 0, 7],
        "requiredunit": None,
        "buildable": True,
        "description": "Produces " + str(Constants.GOLDMINE_PRODUCTION) + " gold a turn each"
    }
    farm = {
        "name": "farm",
        "type": UnitType.BUILDING,
        "stats": [3, 0, 0, 0, 0, 4],
        "requiredunit": None,
        "buildable": True,
        "description": "Expands unit cap by " + str(Constants.FARM_UNIT_EXPANSION)
    }
    armory = {
        "name": "armory",
        "type": UnitType.BUILDING,
        "stats": [3, 0, 0, 0, 0, 5],
        "requiredunit": None,
        "buildable": True,
        "description": "Allows production of spearmen"
    }
    magetower = {
        "name": "mage tower",
        "type": UnitType.BUILDING,
        "stats": [4, 2, 0, 1, 2, 6],
        "requiredunit": None,
        "buildable": True,
        "description": "Immobile and tanky defense building"
    }

    # in no particular order
    allUnitInfo = {
        "spearman": spearman,
        "footman": footman,
        "archer": archer,
        "village": village,
        "gold mine": goldmine,
        "farm": farm,
        "armory": armory,
        "mage tower": magetower
    }
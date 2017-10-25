from gameobjects.units.gameunit import UnitType

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
        "buildable": True
    }
    footman = {
        "name": "footman",
        "type": UnitType.SOLDIER,
        "stats": [2, 1, 2, 1, 1, 1],
        "buildable": True
    }
    archer = {
        "name": "archer",
        "type": UnitType.SOLDIER,
        "stats": [1, 1, 2, 1, 2, 1],
        "buildable": True
    }
    # BUILDING UNITS
    village = {
        "name": "village",
        "type": UnitType.BUILDING,
        "stats": [6, 0, 0, 0, 0, 0],
        "buildable": False
    }
    goldmine = {
        "name": "gold mine",
        "type": UnitType.BUILDING,
        "stats": [3, 0, 0, 0, 0, 4],
        "buildable": True
    }
    wall = {
        "name": "wall",
        "type": UnitType.BUILDING,
        "stats": [4, 0, 0, 0, 0, 3],
        "buildable": True
    }

    # in no particular order
    allUnitInfo = {
        "spearman": spearman,
        "footman": footman,
        "archer": archer,
        "village": village,
        "gold mine": goldmine,
        "wall": wall
    }
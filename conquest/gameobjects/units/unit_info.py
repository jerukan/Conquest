"""
A class documenting all the stats of the units
Stats are om the following order: [maxhealth, attack, speed, availableattacks, range, cost]
"""

class UnitInfo:

    # SOLDIER UNITS
    spearman = {
        "name": "spearman",
        "stats": [2, 2, 3, 1, 1, 2]
    }
    footman = {
        "name": "footman",
        "stats": [2, 1, 2, 1, 1, 1]
    }
    archer = {
        "name": "archer",
        "stats": [1, 1, 2, 1, 2, 1]
    }

    soldiers = [
        spearman,
        footman,
        archer
    ]

    # BUILDING UNITS
    village = {
        "name": "village",
        "stats": [6, 0, 0, 0, 0, 0]
    }
    goldmine = {
        "name": "gold mine",
        "stats": [3, 0, 0, 0, 0, 4]
    }
    wall = {
        "name": "wall",
        "stats": [4, 0, 0, 0, 0, 3]
    }

    buildings = [
        village,
        goldmine,
        wall
    ]
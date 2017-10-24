from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager

class VillageBuilding(GameUnit):

    """
    The lifeline of the player
    Ripripriprip
    """

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.village.get("name"), UnitInfo.village.get("stats"), self.UnitType.BUILDING, SpriteManager.village_sprite, team, position)
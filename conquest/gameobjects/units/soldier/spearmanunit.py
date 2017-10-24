from gameobjects.units.gameunit import GameUnit
from gameobjects.units.unit_info import UnitInfo
from util.spritemanager import SpriteManager

class SpearmanUnit(GameUnit):

    def __init__(self, team, position):
        GameUnit.__init__(self, UnitInfo.spearman.get("name"), UnitInfo.spearman.get("stats"), self.UnitType.SOLDIER, SpriteManager.spearman_sprite, team, position)
from gameobjects.unit_lists import UnitList
from gameobjects.units.unit_info import UnitInfo


class Commands:
    """
    just a class containing all the different commands for menu and game interfaces
    """

    '''all the game commands'''
    def commandBuild(self, board, currentButton, player, position):
        # if the builded unit is a soldier
        if currentButton.unitname in UnitList.buildableSoldiers:
            if len(player.soldierlist) < player.maxUnits:
                for unit in UnitInfo.allUnitInfo:
                    # these dict references are really messy fix later
                    if currentButton.unitname == UnitInfo.allUnitInfo[unit]["name"]:
                        buildedUnit = UnitInfo.allUnitInfo[unit]

                        if not player.money - buildedUnit["stats"][5] < 0:    # compares costs
                            if board.currentSelection.position in board.buildmoves:
                                # what the fuck is happening
                                board.unitlist.append(UnitList.allUnits[buildedUnit["name"]](player, position))
                                player.deductMoney(buildedUnit["stats"][5])

        # if the builded unit is a building
        elif currentButton.unitname in UnitList.buildableBuildings:
            for unit in UnitInfo.allUnitInfo:
                if currentButton.unitname == UnitInfo.allUnitInfo[unit]["name"]:
                    buildedUnit = UnitInfo.allUnitInfo[unit]

                    if not player.money - buildedUnit["stats"][5] < 0:
                        if board.currentSelection.position in board.buildmoves:
                            board.unitlist.append(UnitList.allUnits[buildedUnit["name"]](player, position))
                            player.deductMoney(buildedUnit["stats"][5])
                            player.updateUnitlist(board.unitlist)
                            board.getBuildMoves(player.buildinglist)

        board.unitlist[len(board.unitlist) - 1].onCreation()

    '''all the menu commands'''
    # lul
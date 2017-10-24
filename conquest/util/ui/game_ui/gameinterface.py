from gameobjects.unit_list import UnitList
from gameobjects.units.unit_info import UnitInfo
from util.constants import Constants
from util.ui.baseinterface import BaseInterface
from util.ui.commands import Commands

from .endturnbutton import EndTurnButton
from .unitbuildbutton import UnitBuildButton


class GameInterface(BaseInterface):
    
    commands = {
        "build": False,
        "endTurn": False
    }

    buttons = [
        EndTurnButton(890, 800)
    ]

    unitButtons = [
        UnitBuildButton(30, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.spearman),
        UnitBuildButton(170, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.footman),
        UnitBuildButton(310, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.archer),
        UnitBuildButton(450, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.wall),
        UnitBuildButton(590, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.goldmine)
    ]


    def blankClick(self, mouseposition, mousepressed):
        if mousepressed:
            for button in self.buttons:
                if button.isClicked(mouseposition, mousepressed) or button.clicked:
                    return False
            for button in self.unitButtons:
                if button.isClicked(mouseposition, mousepressed) or button.clicked:
                    return False
            return True


    def getCommand(self, mouseposition, mousepressed):
        for button in self.buttons:
            if button.isClicked(mouseposition, mousepressed):
                self.commands[button.command] = True
                self.currentButton = button
                #return
        for button in self.unitButtons:
            if button.isClicked(mouseposition, mousepressed):
                self.commands[button.command] = True
                self.currentButton = button
                #return


    def runCommands(self, team, board, mousepressed, blankclick):
        if mousepressed:
            if self.commands["endTurn"]:
                self.currentButton = None
                self.commands["endTurn"] = False
                return "endTurn"
            if self.commands["build"]:
                if blankclick:
                    self.currentButton = None
                    self.commands["build"] = False
                elif board.currentSelection is not None and not board.tileOccupied(board.currentSelection):
                    if self.currentButton.unitname in UnitList.soldierList:
                        for unit in UnitInfo.soldiers:
                            if self.currentButton.unitname == unit["name"]:
                                if not team.money - unit["stats"][5] < 0:
                                    if board.currentSelection.position in board.buildmoves:
                                        self.commandlist.commandBuild(UnitList.soldierList[self.currentButton.unitname], team, board.currentSelection.position, board.unitlist)
                                        team.deductMoney(unit["stats"][5])

                    else:
                        for unit in UnitInfo.buildings:
                            if self.currentButton.unitname == unit["name"]:
                                if not team.money - unit["stats"][5] < 0:
                                    if board.currentSelection.position in board.buildmoves:
                                        self.commandlist.commandBuild(UnitList.buildingList[self.currentButton.unitname], team, board.currentSelection.position, board.unitlist)
                                        team.deductMoney(unit["stats"][5])
                                        team.updateUnitlist(board.unitlist)
                                        board.getBuildMoves(team.getBuildings())

                    board.unitlist[len(board.unitlist) - 1].onCreation()
                    self.currentButton = None
                    self.commands["build"] = False
                return "build"
        return None


    def displayInterface(self, window, mouseposition):
        for button in self.buttons:
            button.displaybutton(window)
            if button.isHoveredOver(mouseposition):
                button.highlightbutton("transparentgreen")
        for button in self.unitButtons:
            button.displaybutton(window)
            if button.isHoveredOver(mouseposition):
                button.highlightbutton("transparentgreen")
        if self.currentButton is not None:
            self.currentButton.highlightbutton("transparentlightgreen")
from gameobjects.units.unit_info import UnitInfo
from util.constants import Constants
from util.ui.baseinterface import BaseInterface

from .endturnbutton import EndTurnButton
from .unitbuildbutton import UnitBuildButton


class GameInterface(BaseInterface):
    
    commands = {
        "build": False,
        "endTurn": False
    }

    buttons = [
        EndTurnButton(890, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10)
    ]

    # TODO auto add all the units
    unitButtons = [
        UnitBuildButton(30, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.spearman),
        UnitBuildButton(170, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.footman),
        UnitBuildButton(310, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.archer),
        UnitBuildButton(450, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.wall),
        UnitBuildButton(590, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.goldmine),
        UnitBuildButton(730, Constants.WINDOWHEIGHT - Constants.UNITBUTTONHEIGHT - 10, UnitInfo.farm)
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


    def runCommands(self, player, board, mousepressed, blankclick):
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
                    player.updateUnitlist(board.unitlist)

                    self.commandlist.commandBuild(board, self.currentButton, player, board.currentSelection.position)

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
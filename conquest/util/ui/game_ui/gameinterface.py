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
        EndTurnButton(1000, Constants.WINDOW_HEIGHT - Constants.END_TURN_BUTTON_HEIGHT - 50)
    ]

    # TODO auto add all the units
    unitButtons = [
        UnitBuildButton(30, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.spearman),
        UnitBuildButton(150, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.footman),
        UnitBuildButton(270, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.archer),
        UnitBuildButton(390, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.goldmine),
        UnitBuildButton(510, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.farm),
        UnitBuildButton(630, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 80, UnitInfo.armory),
        UnitBuildButton(30, Constants.WINDOW_HEIGHT - Constants.UNIT_BUTTON_HEIGHT - 10, UnitInfo.magetower)

    ]

    right_margin_middle = (Constants.WINDOW_WIDTH - Constants.RIGHT_MARGIN_SIZE + Constants.WINDOW_WIDTH) / 2


    def getCommand(self, mouseposition, mousepressed):
        for button in self.buttons:
            if button.isClicked(mouseposition, mousepressed):
                self.commands[button.command] = True
                self.currentButton = button
                return
        for button in self.unitButtons:
            if button.isClicked(mouseposition, mousepressed):
                self.commands[button.command] = True
                self.currentButton = button
                return


    def runCommands(self, player, board, mousepressed, mousepos):
        if mousepressed:
            if self.commands["endTurn"]:
                self.currentButton = None
                self.commands["endTurn"] = False
                return "endTurn"

            elif self.commands["build"]:
                if board.currentSelection is not None and not board.tileOccupied(board.currentSelection):
                    player.updateUnitlist(board.unitlist)

                    self.commandlist.commandBuild(board, self.currentButton, player, board.currentSelection.position, self)

                    self.currentButton = None
                    self.commands["build"] = False
                    return "build"
                if not self.currentButton.buttonrect.collidepoint(mousepos[0], mousepos[1]):
                    self.currentButton = None
                    self.commands["build"] = False

            else:
                self.currentButton = None
                self.clearCommands()
                return None

        return None


    def displayUnitInfo(self, window, unitinfo, position=None, player=None):
        if unitinfo is not None:
            window.displayText(unitinfo["name"].capitalize(), self.right_margin_middle, 60, 30, True)
            if unitinfo["requiredunit"] is not None:
                window.displayText("REQUIRES " + unitinfo["requiredunit"].upper() + " TO BUILD", self.right_margin_middle, 120, 20, True)
            window.displayText("Health: " + str(unitinfo["stats"][0]), self.right_margin_middle, 140, 20, True)
            window.displayText("Attack: " + str(unitinfo["stats"][1]), self.right_margin_middle, 160, 20, True)
            window.displayText("Speed: " + str(unitinfo["stats"][2]), self.right_margin_middle, 180, 20, True)
            window.displayText(unitinfo["description"], self.right_margin_middle, 450, 20, True)

            if position is not None and player is not None:
                window.displayText("Current position: " + str(position), self.right_margin_middle, 220, 20, True)
                window.displayText("Player: " + player.color, self.right_margin_middle, 240, 20, True)


    def displayInterface(self, window, mouseposition):
        for button in self.buttons:
            button.displaybutton(window)
            if button.isHoveredOver(mouseposition):
                button.highlightbutton("transparentgreen")
        for button in self.unitButtons:
            button.displaybutton(window)
            if button.isHoveredOver(mouseposition):
                button.highlightbutton("transparentgreen")
                self.displayUnitInfo(window, button.unitinfo)
        if self.currentButton is not None:
            self.currentButton.highlightbutton("transparentlightgreen")
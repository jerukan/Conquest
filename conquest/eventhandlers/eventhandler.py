import pygame, sys
from pygame.locals import *

from eventhandlers.uihandler import UIHandler
from util.ui import *
from util.board_util.board import Board
from util.window import Window
from util.team import Team
from util.constants import Constants

from gameobjects.units import *

# the supreme event handler

class EventHandler:

    pygame.init()

    def __init__(self):
        self.window = Window()
        self.board = Board()

        self.uihandler = UIHandler()

        self.CLOCK = pygame.time.Clock()

        self.currentCommand = None

        self.teamList = [
            Team(1, "red"),
            Team(2, "blue")
        ]

        self.mousepos = []
        self.mousepressed = False

        self.turnEnd = False


    def resetGame(self):
        self.board.generateBoard()
        self.uihandler.setInterface(GameInterface())
        for i in range(0, len(self.teamList)):
            self.board.addUnit(VillageBuilding(self.teamList[i], Constants.VILLAGE_START_POSITIONS[i]))


    def displayGame(self, mousepos):
        self.window.fillSurface()
        self.board.displayBoard(mousepos)
        self.uihandler.displayInterface(self.window, mousepos)


    def blankClick(self):
        return self.board.getSelectedTile() is None and self.uihandler.currentInterface.blankClick(self.mousepos, self.mousepressed)


    def turnStartActions(self, team):
        self.board.resetUnitActions()
        team.updateUnitlist(self.board.unitlist)
        self.board.getBuildMoves(team.getBuildings())
        team.produceMoney()
        for unit in self.board.unitlist:
            unit.onTurnStart()


    def turnEndActions(self):
        for unit in self.board.unitlist:
            unit.onTurnEnd()


    def gameLoop(self):

        for team in self.teamList:
            self.turnEnd = False
            self.turnStartActions(team)
            while not self.turnEnd:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        self.mousepressed = True
                    elif event.type == MOUSEBUTTONUP:
                        self.mousepressed = False

                self.mousepos = pygame.mouse.get_pos()

                self.board.update(self.mousepressed, self.mousepos, team)

                self.uihandler.getInterfaceCommand(self.mousepos, self.mousepressed)

                cmd = self.uihandler.runInterfaceCommands(team, self.board, self.mousepressed, self.blankClick())
                """FUCK"""
                if cmd == "endTurn":
                    self.turnEnd = True

                self.displayGame(self.mousepos)
                self.window.displayText(team.color + "\'s turn", 0, 0, 60)
                self.window.displayText(team.color + "\'s money: " + str(team.money), 600, 0, 50)
                pygame.display.update()

                self.CLOCK.tick(Constants.FPS)
            self.turnEndActions()
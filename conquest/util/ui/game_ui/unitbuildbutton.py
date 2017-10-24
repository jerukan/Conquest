import pygame

from util.colors import Colors
from util.constants import Constants
from util.ui.button import Button


class UnitBuildButton(Button):

    command = "build"

    def __init__(self, x, y, unitinfo):
        self.unitinfo = unitinfo
        self.unitname = self.unitinfo["name"]
        Button.__init__(self, x, y, Constants.UNITBUTTONWIDTH, Constants.UNITBUTTONHEIGHT, self.command, self.unitname)


    def displaybutton(self, window):
        pygame.draw.rect(window.SURFACE, Colors.colorlist['black'], self.buttonrect, 2)
        window.displayText(self.text, self.buttonrect.centerx, self.buttonrect.centery, 30, True)
        window.displayText("Cost: " + str(self.unitinfo["stats"][5]), self.buttonrect.left + 5, self.buttonrect.bottom - 20, 20)
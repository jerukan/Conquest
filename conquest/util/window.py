import pygame

from .constants import Constants
from .colors import Colors

class Window:

    SURFACE = pygame.display.set_mode((Constants.WINDOWWIDTH, Constants.WINDOWHEIGHT))

    pygame.display.set_caption(Constants.GAMENAME)

    def fillSurface(self):

        self.SURFACE.fill(Constants.BACKGROUNDCOLOR)


    def displayText(self, text, x, y, fontsize, centered = False):
        font = pygame.font.SysFont(None, fontsize)
        textObj = font.render(text, True, Colors.colorlist['black'])
        textRect = textObj.get_rect()
        if centered:
            textRect.center = (x, y)
        else:
            textRect.topleft = (x, y)
        self.SURFACE.blit(textObj, textRect)
import pygame, random
from util.constants import Constants
from util.colors import Colors
from util.window import Window
from util.spritemanager import SpriteManager

class Tile:

    """
    One of the many tiles that are on the board

    :parameter xpos: horizontal position of the tile model on the window
    :parameter ypos: vertical position of the tile model on the window
    :parameter position ([height, width]): index on the board the tile is located on

    :var model (Rect): the rectangle object that represents the tile. currently in a permanent location.
    :var selected (bool): if the tile has been selected by any means
    """

    def __init__(self, xpos, ypos, position):
        self.rect = pygame.Rect((xpos, ypos), (Constants.TILE_SIZE, Constants.TILE_SIZE))

        self.tileSprite = SpriteManager.tileList[random.randint(0, len(SpriteManager.tileList) - 1)]
        self.selected = False

        self.position = position


    def isHovered(self, mousepos):
        return self.rect.collidepoint(mousepos[0], mousepos[1])


    def highlight(self, color):
        highlightSurface = pygame.Surface((self.rect.width, self.rect.height))
        highlightSurface = highlightSurface.convert_alpha()
        highlightSurface.fill(Colors.colorlist[color])
        Window.SURFACE.blit(highlightSurface, self.rect.topleft)


    def displayTile(self):
        Window.SURFACE.blit(self.tileSprite, self.rect)
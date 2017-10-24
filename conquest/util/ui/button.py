import pygame;
from util.colors import Colors
from util.window import Window


class Button:

    """
    Like a tile but it's for other stuff

    :parameter x: horizontal position on the window
    :parameter y: vertical position on the window
    :parameter command (str): name of the command this button should execute when clicked, defined in UIHandler
    :parameter text (str): text you want in the button
    """

    def __init__(self, x, y, width, height, command, text):
        self.position = [x, y]
        self.width = width
        self.height = height

        self.command = command

        self.text = text

        self.buttonrect = pygame.Rect(x, y, self.width, self.height)

        self.clicked = False


    def isHoveredOver(self, mousehoverposition):
        if self.buttonrect.collidepoint(mousehoverposition[0], mousehoverposition[1]):
            return True
        return False


    def highlightbutton(self, color):
        highlightSurface = pygame.Surface((self.buttonrect.width, self.buttonrect.height))
        highlightSurface = highlightSurface.convert_alpha(Window.SURFACE)
        highlightSurface.fill(Colors.colorlist[color])
        Window.SURFACE.blit(highlightSurface, self.buttonrect.topleft)


    def displaybutton(self, window):
        pygame.draw.rect(window.SURFACE, Colors.colorlist['black'], self.buttonrect, 2)
        window.displayText(self.text, self.buttonrect.centerx, self.buttonrect.centery, 30, True)


    def isClicked(self, mouseposition, mousepressed):
        if mousepressed:
            if self.isHoveredOver(mouseposition):
                if not self.clicked:
                    self.clicked = True
                else:
                    return False
        else:
            self.clicked = False
        return self.clicked
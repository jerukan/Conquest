from util.ui.commands import Commands

class BaseInterface:

    commandlist = Commands()
    currentButton = None
    buttons = []    # list of all the buttons for an interface (likely grouped into different cool stuff)
    commands = {}   # dictionary with all the strings corresponding to commands, and whether they're running


    def blankClick(self, mouseposition, mousepressed):
        if mousepressed:
            for button in self.buttons:
                if button.isClicked(mouseposition, mousepressed) or button.clicked:
                    return False
            return True


    def getCommand(self, mouseposition, mousepressed):
        for button in self.buttons:
            if button.isClicked(mouseposition, mousepressed):
                self.commands[button.command] = True
                self.currentButton = button
                #return


    def clearCommands(self):
        for i in range(0, len(self.commands)):
            self.commands[i] = False


    def runCommands(self, team, board, mousepressed, blankclick):
        pass


    def displayInterface(self, window, mouseposition):
        for button in self.buttons:
            button.displaybutton()
            if button.isHoveredOver(mouseposition):
                button.highlightbutton("transparentgreen")
        if self.currentButton is not None:
            self.currentButton.highlightbutton("transparentlightgreen")
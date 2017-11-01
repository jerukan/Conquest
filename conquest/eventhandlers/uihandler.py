class UIHandler:

    currentInterface = None

    def setInterface(self, interface):
        if self.currentInterface is not None:
            self.currentInterface.clearCommands()
        self.currentInterface = interface


    def blankClick(self, mouseposition, mousepressed):
        self.currentInterface.blankClick(mouseposition, mousepressed)


    def getInterfaceCommand(self, mouseposition, mousepressed):
        self.currentInterface.getCommand(mouseposition, mousepressed)


    def runInterfaceCommands(self, team, board, mousepressed, mousepos):
        return self.currentInterface.runCommands(team, board, mousepressed, mousepos)


    def displayInterface(self, window, mouseposition):
        self.currentInterface.displayInterface(window, mouseposition)
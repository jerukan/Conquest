class Commands:
    """just a class containing all the different commands for menu and game interfaces"""

    '''all the game commands'''
    def commandBuild(self, unit, team, position, unitlist):
        unitlist.append(unit(team, position))

    '''all the menu commands'''
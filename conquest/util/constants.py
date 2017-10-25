from util.colors import Colors

class Constants:
    """
    Cool constants
    Names are self explanatory
    Hopefully
    """

    '''Game setup and display settings'''
    GAMENAME = "Conquest"

    # number of spaces
    BOARDWIDTH = 10
    BOARDHEIGHT = 6

    BACKGROUNDCOLOR = Colors.colorlist['white']

    TILESIZE = 120  # pixels

    UNITBUTTONWIDTH = 130
    UNITBUTTONHEIGHT = 90

    ENDTURNBUTTONWIDTH = 150
    ENDTURNBUTTONHEIGHT = 70

    UNITSCALESIZE = 0.7

    MARGINSIZE = 50

    WINDOWWIDTH = (BOARDWIDTH * TILESIZE) + (MARGINSIZE * 2)
    WINDOWHEIGHT = (BOARDHEIGHT * TILESIZE) + (MARGINSIZE * 2) + 100

    FPS = 30

    '''Gameplay constants'''
    MAX_TEAMS = 4

    # all the positions a unit away from the corners, ordered diagonally for reasons
    VILLAGE_START_POSITIONS = [[1, 1], [BOARDHEIGHT - 2, BOARDWIDTH - 2], [BOARDHEIGHT - 2, 1], [1, BOARDWIDTH - 2]]

    DEFAULT_STARTING_MONEY = 3
    DEFAULT_MONEY_PRODUCTION = 1

    GOLDMINE_PRODUCTION = 2
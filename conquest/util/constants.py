from util.colors import Colors

class Constants:
    """
    Cool constants
    Names are self explanatory
    Hopefully
    """

    '''Game setup and display settings'''
    # most sizes are in pixels
    GAME_NAME = "Conquest"

    # number of spaces
    BOARD_WIDTH = 15
    BOARD_HEIGHT = 8

    BACKGROUND_COLOR = Colors.colorlist['white']

    TILE_SIZE = 90

    UNIT_SCALE = 0.7

    LEFT_MARGIN_SIZE = 50
    RIGHT_MARGIN_SIZE = 300
    TOP_MARGIN_SIZE = 50
    BOTTOM_MARGIN_SIZE = 150

    WINDOW_WIDTH = (BOARD_WIDTH * TILE_SIZE) + LEFT_MARGIN_SIZE + RIGHT_MARGIN_SIZE
    WINDOW_HEIGHT = (BOARD_HEIGHT * TILE_SIZE) + TOP_MARGIN_SIZE + BOTTOM_MARGIN_SIZE

    FPS = 30

    '''buttons'''
    UNIT_BUTTON_WIDTH = 110
    UNIT_BUTTON_HEIGHT = 60

    END_TURN_BUTTON_WIDTH = 150
    END_TURN_BUTTON_HEIGHT = 70

    '''Gameplay constants'''
    MAX_TEAMS = 4

    # all the positions a unit away from the corners, ordered diagonally for reasons
    VILLAGE_START_POSITIONS = [[1, 1], [BOARD_HEIGHT - 2, BOARD_WIDTH - 2], [BOARD_HEIGHT - 2, 1], [1, BOARD_WIDTH - 2]]

    DEFAULT_STARTING_MONEY = 3
    DEFAULT_MONEY_PRODUCTION = 2
    DEFAULT_MAX_UNITS = 3

    GOLDMINE_PRODUCTION = 2
    FARM_UNIT_EXPANSION = 3
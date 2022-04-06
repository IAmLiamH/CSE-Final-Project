from game.shared.color import Color
import os

# Just a list of constants for reference elsewhere, nothing to see here.
COLUMNS = 32
ROWS = 32
CELL_SIZE = 16
MAX_X = 512
MAX_Y = 512
FRAME_RATE = 15
FONT_SIZE = 25
CAPTION = "Team 6's Platformer"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

LEVEL1 = os.path.dirname(os.path.abspath(__file__)) + "/data/level1.txt"

MAX_SPEED_NORTH = 10
MAX_SPEED_EAST = 5
MAX_SPEED_SOUTH = 5
MAX_SPEED_WEST = 5
from game.shared import constants as constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._red_direction = Point(0, -constants.CELL_SIZE)
        # self._blue_direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        cycles = cast.get_actors("cycles")
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._red_direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._red_direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._red_direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._red_direction = Point(0, constants.CELL_SIZE)
        
        red_cycle = cycles[0]
        

        # # left
        # if self._keyboard_service.is_key_down('j'):
        #     self._blue_direction = Point(-constants.CELL_SIZE, 0)
        
        # # right
        # if self._keyboard_service.is_key_down('l'):
        #     self._blue_direction = Point(constants.CELL_SIZE, 0)
        
        # # up
        # if self._keyboard_service.is_key_down('i'):
        #     self._blue_direction = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('k'):
        #     self._blue_direction = Point(0, constants.CELL_SIZE)
        
        # blue_cycle = cycles[1]
        # blue_cycle.turn_head(self._blue_direction)
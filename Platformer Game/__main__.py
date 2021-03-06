
from game.shared import constants as constants
# from game.shared.constants import constants as Constants

from game.casting.cast import Cast
from game.casting.block import Block
# from game.casting.score import Score
from game.casting.player import Player

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.populate_block_cast_action import PopulateBlockCastAction
from game.scripting.draw_actors_action import DrawActorsAction
# from game.scripting.handle_gravity_action import HandleGravityAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.shared.constants import CELL_SIZE

def main():
    
    # create the cast
    cast = Cast()
    script = Script()
    player = Player()
    
    
    
    # score_one = Score("One")
    
    # block.set_position(Point(100, 100))
    player.prepare_body()



    # level1_populated_blocks = PopulateBlockCastAction(constants.LEVEL1)
    # level2_populated_blocks = PopulateBlockCastAction(constants.LEVEL2)
    # level3_populated_blocks = PopulateBlockCastAction(constants.LEVEL3)
    
    populated_blocks = PopulateBlockCastAction(constants.LEVEL2)
    populated_blocks.get_populated_block_cast()
    for split_block in populated_blocks.get_populated_block_cast():
        x = int(split_block[1]) * CELL_SIZE
        y = int(split_block[2]) * CELL_SIZE
        c = split_block[3]

        if c == "c_green":
            block_color = constants.GREEN
        elif c =="c_gray":
            block_color = constants.GRAY
        elif c =="c_blue":
            block_color = constants.BLUE
        elif c =="c_black":
            block_color = Color(0, 0, 0)
        elif c =="c_white":
            block_color = Color(255, 255, 255)
        elif c =="c_red":
            block_color = constants.RED
        else:
            pass

        
        new_block = Block(x,y, block_color)
        cast.add_actor("blocks", new_block)

        # Testing line V
        # print(f"New block being added.\nX: {x}, Y: {y}")
        # print(split_block)
    


    cast.add_actor("player", player)
    # cast.add_actor("blocks", block)
    
    # score_one.prepare_score("One")
    
    
    # cast.add_actor("scores", score_one)
    
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    
    script.add_action("input", ControlActorsAction(keyboard_service))

    script.add_action("update", MoveActorsAction())
    
    script.add_action("update", HandleCollisionsAction(cast))
    
    script.add_action("output", DrawActorsAction(video_service))

    #Testing line:
    # PopulateBlockCastAction.execute(cast, script)

    
    director = Director(video_service)
    director.start_game(cast, script)
    


if __name__ == "__main__":
    main()


# # cast.add_actor("cycles", Snake())
# # cast.add_actor("cycles", Snake())

# #-----

# cycles = cast.get_all_actors("cycles")

# red_cycle = cycles[0]
# blue_cycle = cycles[1]


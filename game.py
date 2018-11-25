"""
The game module
    - coordinate everything and run the game
    - call pyglet window, various backend and frontend functions
    - choose standard or other map to be loaded
"""

import backend
import frontend
import pyglet
import sys

# load JSON map data from the backend module
if len(sys.argv) == 1:
    map_name = "maps/test_3.json"

# if other map should be loaded, use extra argument "maps/MAP_NAME.json" when calling game.py by Python
        # for example: python game.py maps/test_2.json
else:
    map_name = sys.argv[1]

data = backend.get_data(map_name)

# load pyglet graphic window from the frontend module
window = frontend.init_window(frontend.WINDOW_WIDTH, frontend.WINDOW_HEIGHT)


state = backend.get_start_state(data)

@window.event
def on_draw():
    """
    clear the graphic window
    and finally draw the board game
    """

    # load pyglet sprites by the frontend module
    images = frontend.load_images(state, frontend.TILE_WIDTH, frontend.TILE_HEIGHT)
    robots = frontend.load_robots(state, frontend.TILE_WIDTH, frontend.TILE_HEIGHT)

    window.clear()
    frontend.draw_board(images, robots)

def move_once(t):
    """
    move all robots 2 tiles forward
    """

    for robot in state.robots:
        robot.walk(2)

pyglet.clock.schedule_once(move_once, 3)

# this runs the pyglet library
pyglet.app.run()

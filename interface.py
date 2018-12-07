from enum import Enum
import pyglet
from pyglet.window import key

window = pyglet.window.Window(768, 1024)
press_key = set()
A = (47, 567)
#data = [coordinate of first element, number of elements, space between elements, path]

class InterfaceData(Enum):
    interface = (0, 0),1, 0,'interface/png/interface.png'
    lives = (354, 864), 3, 46, 'interface/png/life.png'
    indicator = (688, 864), 1, 0, 'interface/png/green.png'
    flags = (332, 928), 8, 48, 'img/squares/png/flag_{}.png'
    tokens = (676, 768), 10, -70, 'interface/png/token.png'
    power_down = (186, 854), 1, 0, 'interface/png/power.png'



    def __init__(self, first_coordinates, elements_count, space, path):
        self.first_coordinates = first_coordinates
        self.elements_count = elements_count
        self.space = space
        self.path = path


def create_sprites(element):
    sprites = []
    for i in range(element.elements_count):
        x, y = element.first_coordinates
        x = x + i * element.space
        img = pyglet.image.load(element.path.format(i+1))
        sprite = pyglet.sprite.Sprite(img, x, y)
        sprites.append(sprite)
    print(sprites)
    return sprites


def get_element(InterfaceData_element):
    sprites = create_sprites(InterfaceData_element)
    return sprites


def draw_interface(sprites):
    for tile_sprite in sprites:
        tile_sprite.draw()


@window.event
def on_draw():
    window.clear()
    draw_interface(create_sprites(InterfaceData.interface)) # background


    if ('power', 1) in press_key:
        draw_interface(get_element(InterfaceData.power_down))




@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.P:
        press_key.add(('power', 1))
    if symbol == key.O:
        press_key.discard(('power', 1))



pyglet.app.run()

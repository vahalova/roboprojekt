from enum import Enum
import pyglet
from pyglet.window import key

window = pyglet.window.Window(768, 1024)
press_key = set()
press_key_card = set()

robot_injury = 3 #provisional value



#data = [coordinate of first element, number of elements, space between elements, path]
class InterfaceData(Enum):
    interface = (0, 0),1, 0,'interface/png/interface.png'
    lives = (354, 864), 3, 46, 'interface/png/life.png'
    indicator = (688, 864), 1, 0, 'interface/png/green.png'
    flags = (332, 928), 8, 48, 'img/squares/png/flag_{}.png'
    tokens = (676, 768), 10, -70, 'interface/png/token.png'
    power_down = (186, 854), 1, 0, 'interface/png/power.png'
    cards_1 = (47, 384), 5, 144, 'interface/png/card_bg.png'
    cards_2 = (120, 224), 4, 144, 'interface/png/card_bg.png'
    cards_3 = (47, 576), 5, 144, 'interface/png/card_bg.png'


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
    return sprites


def get_element(InterfaceData_element):
    sprites = create_sprites(InterfaceData_element)
    return sprites


def draw_interface(sprites):
    for tile_sprite in sprites:
        tile_sprite.draw()

def get_cards():
    card_count = InterfaceData.cards_1.elements_count+InterfaceData.cards_2.elements_count-robot_injury
    path = 'interface/png/card_bg.png'
    InterfaceData.cards_1.path = path
    InterfaceData.cards_2.path = path

    sprites_1_row = []
    sprites_1_row.extend(get_element(InterfaceData.cards_1))
    sprites_1_row.extend(get_element(InterfaceData.cards_2))
    draw_interface(sprites_1_row[0:card_count])


    path = 'interface/png/card_stop.png'
    InterfaceData.cards_1.path = path
    InterfaceData.cards_2.path = path

    sprites_2_row = []
    sprites_2_row.extend(get_element(InterfaceData.cards_1))
    sprites_2_row.extend(get_element(InterfaceData.cards_2))
    draw_interface(sprites_2_row[card_count:])


@window.event
def on_draw():
    window.clear()
    draw_interface(create_sprites(InterfaceData.interface)) # background
    draw_interface(get_element(InterfaceData.tokens)[:robot_injury])
    get_cards()



    if ('power', 1) in press_key:
        draw_interface(get_element(InterfaceData.power_down))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.P: # turn off the power
        press_key.add(('power', 1))

    if symbol == key.O: # turn on the power
        press_key.discard(('power', 1))

    if symbol == key.Q:
        press_key.add(('Q', 1))

    if symbol == key._1:
        press_key_card.add(('1', 1))

    return press_key, press_key_card


pyglet.app.run()

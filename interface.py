from enum import Enum
import pyglet


window = pyglet.window.Window(768, 1024)

#data = [coordinate of first element, number of elements, space between elements, path]

class InterfaceData(Enum):
    interface = (0, 0),1, 0,'interface/png/interface.png'
    lives = (354, 864), 2, 46, 'interface/png/life.png'
    indicator = (688, 864), 1, 0, 'interface/png/green.png'
    flags = (332, 928), 3, 48, 'img/squares/png/flag_{}.png'
    tokens = (670, 416), 3, -78, 'interface/png/token.png'

    def __init__(self, first_coordinates, elements_count, space, path):
        self.first_coordinates = first_coordinates
        self.elements_count = elements_count
        self.space = space
        self.path = path

def create_sprites():
    sprites = []
    for element in InterfaceData:
        for i in range(element.elements_count):
            x, y = element.first_coordinates
            x = x + i * element.space
            img = pyglet.image.load(element.path.format(i+1))
            sprite = pyglet.sprite.Sprite(img, x ,y)
            sprites.append(sprite)
    return sprites

def draw_interface(sprites):
    for tile_sprite in sprites:
        tile_sprite.draw()


@window.event
def on_draw():
    window.clear()
    sprites = create_sprites()
    draw_interface(sprites)

pyglet.app.run()

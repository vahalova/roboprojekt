import pyglet


window = pyglet.window.Window(768,1024)


#data = [coordinate of first element, number of elements, space between elements, path]
interface_data = [(0, 0),1, 0,'interface/png/interface.png']
lives_data = [(354, 864), 2, 46, 'interface/png/life.png']
indicator_data = [(688, 864), 1, 0, 'interface/png/green.png']
flags_data = [(332, 928), 3, 48, 'img/squares/png/flag_{}.png']
tokens_data = [(670, 416), 3, -78, 'interface/png/token.png']


def interface_sprites(data):
    sprites = []
    print(data)
    for i in range(data[1]):
        x, y = data[0]
        x = x + i*data[2]
        img = pyglet.image.load(data[3].format(i+1))
        sprite = pyglet.sprite.Sprite(img, x ,y)
        sprites.append(sprite)
    return sprites


def draw_interface(interface_backend, lives, flags, tokens, green):
    tile_sprites = []
    tile_sprites.extend(interface_backend)
    tile_sprites.extend(lives)
    tile_sprites.extend(flags)
    tile_sprites.extend(tokens)
    tile_sprites.extend(green)
    print(tile_sprites)
    for tile_sprite in tile_sprites:
        tile_sprite.draw()


@window.event
def on_draw():
    window.clear()
    interface_backend = interface_sprites(interface_data)
    lives = interface_sprites(lives_data)
    flags = interface_sprites(flags_data)
    tokens = interface_sprites(tokens_data)
    green = interface_sprites(indicator_data)
    draw_interface(interface_backend, lives, flags, tokens, green)


pyglet.app.run()

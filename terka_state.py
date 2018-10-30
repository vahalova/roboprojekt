import json
import pyglet


with open('maps/test_3.json') as f:
    map_data = json.loads(f.read())

MAP_WIDTH = map_data['width']
MAP_HEIGHT = map_data['height']
TILE_HEIGHT = map_data['tileheight']
TILE_WIDTH = map_data['tilewidth']

#seznam cisel obrazku
img_numbers=[]
for a in range(len(map_data['layers'])):
    img_numbers.append(map_data['layers'][a]['data'])

#vytvoreni dvojic souradnic
coordinates = []
#reversed protoze mapu mame od vrchu a pyglet vykresluje odspodu
for y in reversed(range(MAP_HEIGHT)):
    for x in range(MAP_WIDTH):
        coordinates.append((x, y))

#vytvoreni seznamu slovniku podle poctu vrstev
coordinates_with_img_numbers = []
for _ in range(len(img_numbers)):
    coordinates_with_img_numbers.append({})

#vytvoreni slovniku souradnic a prislusnych obrazku
for e in range(len(coordinates_with_img_numbers)):
    for i in range(len(coordinates)):
        #pridá do slovniku postupně souradnice a prislusne cislo obrazku
        #vznikne slovnik souranic a cisel obrazku{(0,11):[7].....}
        # 0 je prázdné políčko, to ukládat nechceme
        if img_numbers[e][i] > 0:
            coordinates_with_img_numbers[e][coordinates[i]] = img_numbers[e][i]

#cesta ke slovniku obrazku
tiles = map_data['tilesets'][0]['tiles']
#slovnik id obrazku a cest
img_dict = {}
for img_data in tiles:
    for _ in img_data:
        #vytahnuti cesty k obrazku ze slovniku
        img_path = img_data["image"]
        #toto je uprava cesty, ktera neni uplne ok, ale nechce se mi to vymyslet jinak
        img_path = img_path[3:]
        img_number = img_data["id"]
    #vznkne slovnik {"3":'"cesta"/obrazek.png', ....}
    # +1 kvůli rozdilu id obrazku a cisla obrazku
    img_dict[int(img_number)+1] = img_path


window = pyglet.window.Window(TILE_WIDTH*MAP_WIDTH, TILE_HEIGHT*MAP_HEIGHT)

def draw_imgs():
    window.clear()
    for coordinate_with_img_number in coordinates_with_img_numbers:
        for coordinate, number in coordinate_with_img_number.items():
                #takovy ty kouzla od Petra
                #prevedeni cisla plochy na cislo obrazku
                transferred_number = number & 0xFFFFFF
                #vytahnuti cisla otoceni z cisla plochy
                rotation_number = number>>(4*7)
                #hodnoty pro otocene obrazky
                #obrazky se otaci kolem 0,0, takze je musime posunout zpet na sve misto
                if rotation_number == 0:
                    angle_of_rotation = 0
                    move_x = 0
                    move_y = 0
                elif rotation_number == 10:
                    angle_of_rotation = 90
                    move_x = 0
                    move_y = TILE_HEIGHT
                elif rotation_number == 12:
                    angle_of_rotation = 180
                    move_x = TILE_WIDTH
                    move_y = TILE_HEIGHT
                elif rotation_number == 6:
                    angle_of_rotation = 270
                    move_x = TILE_WIDTH
                    move_y = 0
                #cesta k obrazku podle prevedeneho cisla
                path = img_dict[transferred_number]
                img = pyglet.image.load(path)
                #obrazek, souradnice*sirka/vyska policka + posun podle otoceni
                square = pyglet.sprite.Sprite(img, x = (coordinate[0]*TILE_WIDTH+move_x), y = (coordinate[1]*TILE_HEIGHT+move_y))
                square.rotation = angle_of_rotation
                square.draw()

window.push_handlers(on_draw = draw_imgs)

pyglet.app.run()

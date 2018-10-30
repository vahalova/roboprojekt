import json
import pyglet


with open('maps/test_3.json') as f:
    map_data = json.loads(f.read())

MAP_WIDTH = map_data['width']
MAP_HEIGHT = map_data['height']
TILE_HEIGHT = map_data['tileheight']
TILE_WIDTH = map_data['tilewidth']

#list of image numbers
img_numbers=[]
for item in map_data['layers']:
    img_numbers.append(item['data'])

#list of coordinate pairs [(O, 11), (1, 11),...
coordinates = []
#reversed bcs the map from Tiled start at the top and pygle at bottom
for y in reversed(range(MAP_HEIGHT)):
    for x in range(MAP_WIDTH):
        coordinates.append((x, y))

#empty list of dictionaries
coordinates_with_img_numbers = []
for _ in img_numbers:
    coordinates_with_img_numbers.append({})

#dictionary of coordinates and img numbers {(0, 11): 7,.....}
for e in range(len(coordinates_with_img_numbers)):
    for i in range(len(coordinates)):
        # 0 bcs it is an empty square
        if img_numbers[e][i] > 0:
            coordinates_with_img_numbers[e][coordinates[i]] = img_numbers[e][i]


tiles = map_data['tilesets'][0]['tiles']
#Dictionary of id images and paths {"3":'"path"/img.png', ....}
img_dict = {}
for img_data in tiles:
    for _ in img_data:
        img_path = img_data["image"][3:] #XXX
        img_number = img_data["id"]
    # +1 bcs there is a difference between img id and img number
    img_dict[int(img_number) + 1] = img_path


window = pyglet.window.Window(TILE_WIDTH*MAP_WIDTH, TILE_HEIGHT*MAP_HEIGHT)

def draw_imgs():
    window.clear()
    for coordinate_with_img_number in coordinates_with_img_numbers:
        for coordinate, number in coordinate_with_img_number.items():
                #TODO sry, I don't know, this is magic :-D
                #recalculate number to image number
                transferred_number = number & 0xFFFFFF
                #recalculate number to rotation number
                rotation_number = number>>(4*7)
                if rotation_number == 0:
                    angle_of_rotation = 0
                    #moving images due to rotation around 0,0
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
                #path to image
                path = img_dict[transferred_number]
                img = pyglet.image.load(path)
                #adding an image to the coordinates
                square = pyglet.sprite.Sprite(img, x = (coordinate[0] * TILE_WIDTH + move_x), y = (coordinate[1] * TILE_HEIGHT + move_y))
                square.rotation = angle_of_rotation
                square.draw()

window.push_handlers(on_draw = draw_imgs)

pyglet.app.run()

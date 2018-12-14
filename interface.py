from random import shuffle
from backend import Robot,Direction

life = Robot(Direction.N,"./img/robots_map/png/MintBot.png" , (4,4))
print(life.lifecount)

class InterfaceState:
    def __init__(self, cards, injury, life, power_down, flags):
        self.cards = cards
        self.injury = injury
        self.life = life
        self.power_down = power_down
        self.flags = flags



    def __repr__(self):
        return "<InterfaceState {} Injury:{}, Life:{} Power Down:{} Flags:{}>".format(self.cards, self.injury, self.life, self.power_down, self.flags )


def interface_state():
    deal_cards_list = deal_cards()
    injury = get_robot_injury()
    my_life = get_robot_life()
    power_down = get_power_down()
    flags = get_flags()

    return deal_cards_list, injury, my_life, power_down, flags

def get_deck_of_cards():
    cards_type = {'u_turn': [6, 50, 56],
        'back_up': [5, 250, 255],
        'left': [18, 100, 118],
        'right': [18, 200, 218],
        'move1': [17, 300, 317],
        'move2': [12, 400, 412],
        'move3': [6, 500, 506]
    }
    deck_of_cards = []
    for name, number in cards_type.items():
        for i in range(number[1],number[2]):
            deck_of_cards.append((name, i))
    shuffle(deck_of_cards)
    return(deck_of_cards)


def deal_cards():
    deck_of_cards = get_deck_of_cards()
    deal_cards_list = {}
    for i in range(9-get_robot_injury()):
        deal_cards_list[i+1] =  deck_of_cards.pop()
    return deal_cards_list


def get_robot_injury():
    injury = 0#provisional value
    return injury

def get_robot_life():
    my_life = 3 #provisional value
    return my_life

def get_power_down():
    return False #provisional value

def get_flags():
    flags = 0 #provisional value
    return flags

def get_start_interface_state():
    cards = deal_cards()
    injury = get_robot_injury()
    life = get_robot_life()
    power_down = get_power_down()
    flags = get_flags()
    interface_state = InterfaceState(cards, injury, life, power_down, flags )
    return interface_state

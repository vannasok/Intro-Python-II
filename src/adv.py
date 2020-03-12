from room import Room
from player import Player
from item import Item


# list of items
map = Item('map', 'map of the land')
stick = Item('sticks', 'Wooden stick')
torch = Item('torch', 'bright up the road')
chest = Item('chest', 'gold in chest')
key = Item('key', 'key for the door')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [map, key]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [torch, chest]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [chest, key]),
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Enter player's name:  "), room["outside"])
print("")
print(f'Hi, {player.name}')
print(f'you @ {player.current_room}')

# player.items.append(map)
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def isActionable(cmd):
    tokenList = cmd.split()

    if len(tokenList) == 2:
        for token in tokenList:
            if token in player.react:
                return True
            else:
                return False
    else:
        print('invalid input')
        return False


while True:

    print(player)
    cmd = input(
        "select direction: (n, s, w, e), 'q' to quit 'take/drop item'=> ").lower()
    print('')

    if (cmd == 'q'):
        break
    elif cmd in ['n', 's', 'e', 'w']:
        player.travel(cmd)
    elif isActionable(cmd):
        player.action(cmd)
    else:
        print(f'\nValid Command: {player.react} item')

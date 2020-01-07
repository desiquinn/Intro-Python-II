from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

oscar = Player("Oscar", room['outside'])

direction = ["n", "s", "e", "w"]
# Write a loop that:
#
move = " "
while move not in direction:
# * Prints the current room name
    print(oscar.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(oscar.current_room.description)
    print("Items:")
    for item in oscar.current_room.items:
        print(item)
# * Waits for user input and decides what to do.
    move = input("Which direction would you like to travel?: ")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    if move == "n":
        print("You Moved North")
#    check if room exists
        if oscar.current_room.n_to:
#    move to room to the north
            oscar.current_room = oscar.current_room.n_to
        else: 
            print("You can't move in that direction, no room exsists")
        move = " "

    elif move == "s":
        print("You Moved South")
#    check if room exists
        if oscar.current_room.s_to:
#    move to room to the south
            oscar.current_room = oscar.current_room.s_to
        else: 
            print("You can't move in that direction, no room exsists")
        move = " "

    elif move == "e":
        print("You Moved East")
#    check if room exists
        if oscar.current_room.e_to:
#    move to room to the east
            oscar.current_room = oscar.current_room.e_to
        else: 
            print("You can't move in that direction, no room exsists")
        move = " "

    elif move == "w":
        print("You Moved West")
#    check if room exists
        if oscar.current_room.w_to:
#    move to room to the west
            oscar.current_room = oscar.current_room.w_to
        else: 
            print("You can't move in that direction, no room exsists")
        move = " "

    elif move == "q":
        print("Goodbye!")
#    quit the game
        quit()
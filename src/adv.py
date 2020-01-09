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

# Declare all items

item = {
    'potion': Item("Potion", """One drop of this postion will 
heal you and restore all health"""),

    'sword': Item("Sword", """Protect Yourself from monsters with 
this massive sword"""),
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

# Add Items to rooms

room['foyer'].items.append(item['sword'])
room['overlook'].items.append(item['potion'])

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
    print(f'\n{oscar.current_room.name}')
# * Prints the current description (the textwrap module might be useful here).
    print(oscar.current_room.description)
    if len(oscar.current_room.items) > 0:
        print("Items In Room:")
        for item in oscar.current_room.items:
            print(item)
    else:
        print("This room is empty")
# * Waits for user input and decides what to do.
    move = list(input("""\n(n) - Move North\n(s) - Move South\n(e) - Move East\n(w) - Move West\n(i) - Inventory\n(q) - Quit\n\nWhat would you like to do?: """).split())
    # print(move)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if len(move) == 1: 
        if move[0] == "n":
            print("You Moved North")
#    check if room exists
            if oscar.current_room.n_to:
#    move to room to the north
                oscar.current_room = oscar.current_room.n_to
            else: 
                print("You can't move in that direction, no room exists")

        elif move[0] == "s":
            print("You Moved South")
#    check if room exists
            if oscar.current_room.s_to:
#    move to room to the south
                oscar.current_room = oscar.current_room.s_to
            else: 
                print("You can't move in that direction, no room exists")

        elif move[0] == "e":
            print("You Moved East")
#    check if room exists
            if oscar.current_room.e_to:
#    move to room to the east
                oscar.current_room = oscar.current_room.e_to
            else: 
                print("You can't move in that direction, no room exists")

        elif move[0] == "w":
            print("You Moved West")
#    check if room exists
            if oscar.current_room.w_to:
#    move to room to the west
                oscar.current_room = oscar.current_room.w_to
            else: 
                print("You can't move in that direction, no room exists")

        elif (move[0] == "i") or (move[0] == "inventory"):
            print("\nInventory: ")
            if len(oscar.inventory) > 0:
                for item in oscar.inventory:
                    print(item)
            else:
                print("Your inventory is empty")

        elif move[0] == "q":
            print("Goodbye!")
#    quit the game
            quit()
        
        else:
            print("I don't understand that response")

    elif len(move) == 2:
        if (move[0] == "get") or (move[0] == "take"):
            for item in oscar.current_room.items:
                if item.name == move[1]:
                    oscar.inventory.append(item)
                    oscar.current_room.items.remove(item)
                    item.on_take()
                else:
                    print("No such item exists in this room")
        elif move[0] == "drop":
            for item in oscar.inventory:
                if item.name == move[1]:
                    oscar.current_room.items.append(item)
                    oscar.inventory.remove(item)
                    item.on_drop()
                else:
                    print("You don't have that item")
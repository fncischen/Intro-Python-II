from room import Room
from player import Player

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
player = Player("Current Player", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

key = None

while not key == "q":
	# sleep function // async await wait 3 seconds.

	print("We are inside room:", player.room.name)

	#sleep for x miliseconds to render next line. 

	print("Room description: ", player.room.description )

	print("\n")

	print("List of items in the room",  play.room.Items)

	print("\n")

	print("List of items that player in room", player.room.Items)

	print("Type q if you wish to quit the game")

	key = input("Type which direction, n (North), s (South), e (East) and w (West) to determine which room to enter. Otherwise, type 'take [item name]' or 'drop [item name]' if you see a item you'd like to pick up").split(",")

	# how to split keys: 

	if len(key) <= 1:

		if key == "n":

			if player.room.n_to == None:
				print("This movement is not allowed.")
			else:
				player.room = player.room.n_to


		elif key == "s":
			if player.room.s_to == None:
				print("This movement is not allowed.")
			else:
				player.room = player.room.s_to

		elif key == "e":

			if player.room.e_to == None:
				print("This movement is not allowed.")
			else:
				player.room = player.room.e_to

		elif key == "w":
			if player.room.w_to == None:
				print("This movement is not allowed.")
			else:
				player.room = player.room.w_to

	else:

		if key[0] == "take":

			requestedItem = key[1]
			if requestedItem not in player.room.Items:
				print("This item does not exist in this list of items in the room")
			else:
				player.room.pickUpItem()

		elif key[0] == "drop":

			droppedItem = key[1]
			if droppedItem not in player.Items:
				print("This item does not exist in this list of items per player")
			else:
				player.room.addItem(droppedItem)
				droppedItemIndex = player.Items.index(droppedItem)
				player.Items.pop(droppedItemIndex)

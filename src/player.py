# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, room):
		self.name = name
		self.room = room 
		self.Items = []

	def room():
		return self.room

	def pickUpItem(self, item, room):
		self.Items.append(item)
		roomItemIndex = self.room.Items.index(item)
		self.room.Items.pop(roomItemIndex)
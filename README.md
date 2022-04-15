# lab4_task5

Description of the game.py module to create a game space for the main.py module

## Desccription

There are classes Room, Character, Friend, Enemy and Item for creating a game space. Friend and Enemy are inherited from the Character. 

## Room

Attributes: name, rooms(adjoining rooms), item, character, description.

In method set_description(self, description) the description attribute is created.

link_room(self, next_room, location). Initially, the attribute is equal to a list of four None(four corners of the world). 0 - north, 1 - south, 2 - east, 3 - west. Depending on location, one of the element in a list is changed to instance of the class Room(next_room).

set_character(self, character) changes the attribute self.character to an instance of the Character class or inherited from it. The method set_item(self, item) works similarly.

get_details(self). First, create a string with the attributes self.name and self.description, and then if there are any rooms in the list other than None, then add a string about the location of this room.

get_character and get_item return an instance of the class or None if there no character or item.

move(self, location) According to the indexes and corners of the world mentioned earlier, changes one instance of the class and all its attributes to another, if the list item is not equal to None. If None, print that you cant go there.

## Character

Attributes: name, description, conversation.

set_conversation(self, conversation) Creates a conversation attribute and references the passed argument.

describe() Just prints a string with self.name and self.description

talk() Just prints conversation

## Friend
As there are no friends in main.py, there is just pass

## Enemy

Attributes from Character

set_weakness(self, weakness) Creates a weakness attribute and references the passed argument.

fight(self, weapon). Check if passes argument is equal to self.weakness, changes the global variable num_of_victories which is created before classes, to control game process. Returns True if weapon == self.weakness, the player wins the fight, else returns False and player loses, game is ended.

get_defeated(self) Just returns number_of_victories to control game process.

## Item

Attributes: name, description

In method set_description(self, description) the description attribute is created.

describe() Prints string with self.name and self.description

get_name() returns a name of item to put in back pack

## main.py
This module was not changed

"""Module string"""

number_of_victories = 0


class Character:
    """Class for represenation of character"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def set_conversation(self, conversation: str) -> None:
        """Sets the passed argument instead of the self.conversation"""
        self.conversation = conversation

    def describe(self) -> None:
        """Prints info about character"""
        print(
            f"""
{self.name} is here!
{self.description}
""",
            end="",
        )

    def talk(self) -> None:
        """Prints conversation"""
        print(
            f"""
[{self.name} says]: {self.conversation}
""",
            end="",
        )


class Enemy(Character):
    """Class for represenation of enemy"""

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)

    def set_weakness(self, weakness: str) -> None:
        """Sets the passed argument instead of the self.weakness"""
        self.weakness = weakness

    def fight(self, weapon: str) -> bool:
        """Returns a bool value if is enemy is defeated"""
        if self.weakness == weapon:
            global number_of_victories
            number_of_victories += 1
            return True
        return False

    def get_defeated(self) -> int:
        """Returns number of victories"""
        return number_of_victories


class Friend(Character):
    """Class for represenation of friend"""

    pass


class Item:
    """Class for represenation of item"""

    def __init__(self, name: str) -> None:
        self.name = name

    def set_description(self, description: str) -> None:
        """Sets the passed argument instead of the self.description"""
        self.description = description

    def describe(self) -> None:
        """Prints info about item"""
        print(
            f"""
The [{self.name}] is here - {self.description}
""",
            end="",
        )

    def get_name(self) -> str:
        """Returns name of item"""
        return self.name


class Room:
    """Class for represenation of room"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = [None, None, None, None]
        self.item = None
        self.character = None

    def set_description(self, description: str) -> None:
        """Sets the passed argument instead of the self.description"""
        self.description = description

    def link_room(self, next_room: object, location: str) -> None:
        """Sets the passed argument next_room instead of the self.(location)_room"""
        if location == "north":
            self.rooms[0] = next_room
        elif location == "south":
            self.rooms[1] = next_room
        elif location == "east":
            self.rooms[2] = next_room
        elif location == "west":
            self.rooms[3] = next_room

    def set_character(self, character: Character) -> None:
        """Sets the passed argument instead of the self.character"""
        self.character = character

    def set_item(self, item: Item) -> None:
        """Sets the passed argument instead of the self.item"""
        self.item = item

    def get_details(self) -> None:
        """Prints info about room"""
        details = (
            self.name + "\n" + "--------------------" + "\n" + self.description + "\n"
        )
        for room in self.rooms:
            if room != None:
                if self.rooms.index(room) == 0:
                    location = "north"
                elif self.rooms.index(room) == 1:
                    location = "south"
                elif self.rooms.index(room) == 2:
                    location = "east"
                elif self.rooms.index(room) == 3:
                    location = "west"
                details += f"The {room.name} is {location}\n"
        print(details.rstrip("\n"))

    def get_character(self) -> Character:
        """Returns self.character"""
        return self.character

    def get_item(self) -> Item:
        """Returns self.item"""
        return self.item

    def move(self, location: str):
        """Moves to given room"""
        if location == "north" and self.rooms[0] != None:
            self = self.rooms[0]
        elif location == "south" and self.rooms[1] != None:
            self = self.rooms[1]
        elif location == "east" and self.rooms[2] != None:
            self = self.rooms[2]
        elif location == "west" and self.rooms[3] != None:
            self = self.rooms[3]
        else:
            print(f"You can't go {location}")
        return self

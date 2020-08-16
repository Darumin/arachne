from arachne.game import Game
from arachne.lingo import Desc


class Noun:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.texts: dict = dict()

        self.gettable: bool = False

        # Build a list of unique object IDs.
        Game.add_noun(self)

    def add_description(self, kind: Desc, text: str) -> None:
        if kind in Desc:
            self.texts[kind]: str = text
            print(f"description of kind: {kind} has been set for {self}.")


class Item(Noun):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return "Item-> " + str(id(self))


class Container(Noun):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.contents = dict()

    def __repr__(self) -> str:
        return str(self.contents)

    def add_item(self, item: Item) -> None:
        self.contents[item] = f'{item.name.capitalize()} is here.'

    def remove_item(self, item: Item) -> None:
        try:
            self.contents.pop(item)
        except KeyError:
            print("No such key found. Removal failed.")


class Room(Container):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        # TODO: adjacents = dict()
        # TODO: Should list all adjacent rooms.

    def __repr__(self) -> str:
        return "Room-> " + str(id(self))

    def __len__(self) -> int:
        return self.contents.__len__()

    def describe_room(self) -> str:
        room_desc = self.name + "\n" + self.texts[Desc.SELF]
        room_desc += "\n\n"
        for item in self.contents:
            room_desc += item.texts[Desc.PLACEMENT] + ' '

        return room_desc


class Player(Noun):
    _inventory: dict = dict()
    _player_location: Room = Game.start

    @property
    def inventory(self) -> dict:
        return self._inventory

    @staticmethod
    def store(item_obj: Item):
        Player._inventory[item_obj.name] = item_obj

    @staticmethod
    def get_ids():
        return Player._inventory.values()



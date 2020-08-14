# TODO: Create a player, and an inventory.


class Noun:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.texts: dict = dict()

    def add_description(self, kind: str, text: str) -> None:
        key: str = self.validate_description_kind(kind)
        self.texts[key]: str = text
        print(kind.capitalize() + f' has been set with key [{key}].')

    @staticmethod
    def validate_description_kind(given_kind: str) -> str:
        valid_descriptions: set = {
            'observation',
            'placement'
        }

        if given_kind in valid_descriptions:
            return given_kind[:3]


class Item(Noun):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return str(self.texts)


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
        return f"Room object with title: '{self.name}'"

    def __len__(self) -> int:
        return self.contents.__len__()

    def describe_room(self) -> str:
        room_desc = self.texts['obs']
        for item in self.contents:
            room_desc += ' ' + item.texts['pla']

        return room_desc

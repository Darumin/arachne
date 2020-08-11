# This is a reference for all Nouns or objects/set pieces found in the game.
# TODO: Reevaluate whether strict exceptions are needed here.


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
        raise ValueError(f"'{given_kind}' not valid kind.")


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

    @staticmethod
    def _valid_item(item: Item) -> bool:
        return True if isinstance(item, Item) else False

    def add_item(self, item: Item) -> None:
        if not self._valid_item(item):
            raise TypeError(f"Attempted to add '{item}' ({type(item)}). It is not valid [Item]!")

        self.contents[item] = f'{item.name.capitalize()} is here.'

    def remove_item(self, item: Item) -> None:
        if not self._valid_item(item):
            raise TypeError(f"Given '{item}' is not desired type. Keys are of type [Item]!")

        try:
            self.contents.pop(item)
        except KeyError:
            print("No such key found. Removal failed.")


class Room(Container):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        compass_rose = dict()
        # TODO: Takes a Room object for a key, with optional description.

    def __repr__(self) -> str:
        # TODO: Probably need to move this to a separate function.
        # This should instead return a debugger representation.
        room_desc = self.texts['obs']
        props = ''
        for item in self.contents:
            props += ' ' + item.texts['pla']

        return room_desc + props

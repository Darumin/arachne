class Noun:
    def __init__(self, name):
        self.name = name
        self.texts = dict()

    def add_description(self, kind, text):
        key = self.validate_description_kind(kind)
        self.texts[key] = text
        print(kind.capitalize() + f' has been set with key [{key}].')

    @staticmethod
    def validate_description_kind(given_kind):
        valid_descriptions = {
            'observation',
            'placement'
        }

        if given_kind in valid_descriptions: return given_kind[:3]
        raise KeyError(f"'{given_kind}' not valid kind.")

    @staticmethod
    def validate_container(container_name):
        return True if isinstance(container_name, Container) else False

    @staticmethod
    def validate_item(item_name):
        return True if isinstance(item_name, Item) else False


class Container(Noun):
    def __init__(self, name):
        super().__init__(name)

        self.contents = dict()

    def add_item(self, item):
        # TODO: Maybe lump methods together.
        if not self.validate_item(item): return
        self.contents[item] = f'{item.name.capitalize()} is here.'

    def remove_item(self, item):
        # TODO: Clean this, somewhat.
        if not self.validate_item(item): return
        try:
            self.contents.get(item.name)
        finally:
            self.contents.pop(item.name)

    def __repr__(self):
        return str(self.contents)


class Item(Noun):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return str(self.texts)


class Room(Container):
    def __init__(self, name):
        super().__init__(name)

        compass_rose = dict()
        # TODO: Takes a Room object for a key, with optional description.

    def __repr__(self) -> str:
        room_desc = self.texts['obs']
        props = ''
        for item in self.contents:
            props += ' ' + item.texts['pla']

        return room_desc + props

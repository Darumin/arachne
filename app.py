class Noun:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        pass


class Item(Noun):
    def __init__(self, item_name: str, item_desc: str):
        super().__init__(item_name, item_desc)

        self.can_be_used = False
        self.is_not_possessed = True
        self.description_dict = {
            'item_desc': item_desc,
            'not_carrying': f'{item_name} is here.',
            'carrying': f'You are carrying {item_name.lower()}.'
        }

        self.current_location_desc = self.description_dict['not_carrying']

    def return_desc(self, key: str) -> str:
        return self.description_dict.get(key)

    def set_new_location_description(self, description: str):
        self.current_location_desc = description


class Container(Noun):
    def __init__(self, true_name, description):
        super().__init__(true_name, description)

        self.contents = dict()

    def __repr__(self):
        pass

    def add_item(self, item_name):
        pass


class Room(Container):
    def __init__(self, true_name: str, description: str):
        super().__init__(true_name, description)

    def __repr__(self) -> str:
        set_pieces = ''
        for item in self.contents:
            set_pieces += str(item.current_location_desc) + ' '
        return str(self.name + '\n' + self.description + ' ' + set_pieces)

    def store_item(self, item: Item, description: str = None):
        if not description:
            if item.is_not_possessed:
                default_desc = item.return_desc('not_carrying')
            else:
                default_desc = item.return_desc('carrying')
        else:
            default_desc = description

        self.contents[item] = default_desc
        item.set_new_location_description(default_desc)
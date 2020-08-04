class Item:
    def __init__(self, true_name: str, description: str=None, placement: str=None):
        self.name = true_name
        self.desc = description
        self.placement = placement
        self.is_staged = False

    @property
    def placement_description(self) -> str:
        return self.placement if self.is_staged else ''

class Container:
    def __init__(self, true_name):
        self.name = true_name
        self.contents = list()

    def __repr__(self):
        ret = ''
        for item in self.items:
            ret += str(item) + ', '
        return '\nlabel: ' + self.label + '\nitems: ' + ret + '\n'

    def add_item(self, item_name):
        if not isinstance(item_name, Item):
            return
        item_name.is_staged = True
        self.contents.append(item_name)

class Room(Container):
    def __init__(self, true_name: str, description: str=''):
        super().__init__(true_name)
        self.desc = description
        self.compass_rose = dict()

    def __str__(self) -> str:
        set_pieces = ''
        for item in self.contents:
            set_pieces += item.placement_description + ' '
        return str(self.name + '\n' + self.desc + ' ' + set_pieces)

if __name__ == '__main__':
    room = Room("The Nice Place", "A big room, quite nice.")
    rose = Item("A rose", "It smells sweet", "A rose is growing here.")
    compass = Item("A compass", "Iron, it smells of earth", "The compass is in the corner.")

    room.add_item(rose)
    room.add_item(compass)

    print(room)

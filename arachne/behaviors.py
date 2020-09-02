from functools import partial

from arachne.lingo import Object, Verb, Compass
from arachne.game import _Player
from arachne.nouns import Noun, Container, Item, Room


# the bulk of game behavior is found here
def return_attribute(given: Noun, attribute: str) -> str:
    return getattr(given, attribute)


return_name = partial(return_attribute, attribute="name")
return_examined = partial(return_attribute, attribute="when_examined")
return_contents = partial(return_attribute, attribute="contents")
return_encountered = partial(return_attribute, attribute="when_encountered")
return_unlock_id = partial(return_attribute, attribute="unlock_id")


def handle_go(direction) -> str:
    compass_rose: dict = get_player_location().adjacency
    if direction in compass_rose:
        set_player_location(compass_rose[direction])
        return room_description(get_player_location())
    return "Nothing that way."


def bridge_rooms(room_one: Room, direction, room_two: Room):
    opposite = flip_compass(direction)
    if opposite:
        if direction in room_two.adjacency:
            return
        room_two.adjacency[direction] = room_one
        room_one.adjacency[opposite] = room_two


def flip_compass(initial) -> Compass:
    final = None

    if initial is Compass.NORTH: final = Compass.SOUTH
    elif initial is Compass.EAST: final = Compass.WEST
    elif initial is Compass.WEST: final = Compass.EAST
    elif initial is Compass.SOUTH: final = Compass.NORTH
    elif initial is Compass.NORTHEAST: final = Compass.SOUTHWEST
    elif initial is Compass.NORTHWEST: final = Compass.SOUTHEAST
    elif initial is Compass.SOUTHEAST: final = Compass.NORTHWEST
    elif initial is Compass.SOUTHWEST: final = Compass.NORTHEAST
    elif initial is Compass.UP: final = Compass.DOWN
    elif initial is Compass.DOWN: final = Compass.UP

    return final


def room_description(room: Room) -> str:
    desc: str = return_name(room)
    desc += "\n" + return_examined(room)
    desc += _room_placed_description(room)
    return desc


def _room_placed_description(room: Room) -> str:
    extra: dict = return_contents(room)
    desc: str = ""
    if extra:
        desc += "\n\n"
        for each in extra.values():
            if each.is_concealed is False:
                desc += return_encountered(each) + " "
    return desc


def _inventory() -> dict:
    return _Player.contents


def describe_inventory() -> str:
    carrying: list = list(_inventory().values())

    if any(_inventory()):
        description: str = "You are carrying... \n"
        if len(carrying) > 1:
            for item in carrying[:-1]:
                description += item.name + ", "
            description += "and " + carrying[-1].name + "."
        else:
            description += carrying[0].name + "."
    else: description = "You are not carrying anything."
    return description


def check_inventory(item_str: str) -> bool:
    inv: dict = _inventory()
    for item_id in inv:
        instance = inv[item_id]
        if item_str in instance.name:
            return True
    return False


def add_to_inventory(item: Item) -> None:
    add_to_container(_Player, item)


def free_item(item: Item):
    parent = item.parent_container
    if parent:
        item.parent_container = None
        remove_from_container(parent, item)


def get_player_location():
    return _Player.current_location


def set_player_location(room: Room):
    _Player.current_location = room


def vicinity() -> dict:
    # lump everything within reach of player into one dict
    open_containers = _get_all_open_containers()
    inventory = _inventory()
    return {**open_containers, **inventory}


def _get_all_open_containers() -> dict:
    current_location = get_player_location()
    all_containers = dict()

    for each in current_location.contents:
        noun = current_location.contents[each]
        if isinstance(noun, Container) and not noun.is_sealed:
            all_containers.update(noun.contents)

    return {**current_location.contents, **all_containers}


def add_to_container(storage, item):
    """
    :param storage: can be type _Player, Container, Room
    :param item: can be any type where gettable = True
    any subject may have contents containing items. The _Player's contents is inventory.
    see usage of subject in remove_from_container() as well
    """
    _key: int = id(item)
    if _key not in storage.contents:
        storage.contents[_key] = item
        item.parent_container = storage


def drop_in_room(item: Item):
    item.when_encountered = f"{item.name.capitalize()} is here."
    room_dropped = get_player_location()
    add_to_container(room_dropped, item)


def remove_from_container(storage, item: Item):
    storage.contents.pop(id(item))


def describe_contents(container: Container):
    if container.is_sealed:
        return "\n\nIt is closed."

    if container.contents:
        description = "\n\n"
        values = iter(container.contents.values())

        if len(container.contents) == 1:
            description += f"Inside is {next(values).name}."
        else:
            for item in values:
                description += item.name + ", "
            description = "\n\nInside it are: " + description[2:-2] + "."

        return description
    return "\n\nThere is nothing inside."


def guess_object(object_str: str) -> tuple:
    results: list = list()
    if object_str == "": return Object.UNSPECIFIED, results

    # check vicinity (everywhere except inventory) for closest matching subject
    vic: dict = vicinity()
    for object_id in vic:
        instance = vic[object_id]
        if object_str in instance.name and not instance.is_concealed:
            results.append(instance)

    # check what kind of subject input this is
    typified = _typify_object(object_str, len(results))

    # if multiple matches, resolve the matches
    # if nonexistent, create a list with one entry for the sake of returning a valid tuple
    if typified is Object.MULTIPLE: return _resolve_multiple(results)
    if typified is Object.NONEXISTENT: results.append(Object.NONEXISTENT)

    # finally return this tuple if nothing else applies
    return typified, results[0]


def _typify_object(object_str: str, amount_found: int) -> Object:
    if object_str == "all": return Object.ALL
    if amount_found == 0: return Object.NONEXISTENT
    if amount_found > 1: return Object.MULTIPLE
    if check_inventory(object_str): return Object.POSSESSED
    return Object.FOUND


def _resolve_multiple(results: list):
    print("Which one?")

    for result in enumerate(results, start=1):
        print(f"{result[0]})", result[1].name, end=" ")

    choice: str = input("\n>")
    return guess_object(choice)


def check_key_for(container: Container):
    for each in _inventory().values():
        unlock_id = return_unlock_id(each)
        if unlock_id == id(container):
            return each.name
    return False


def lock_switch_output(verb: Verb, openable):
    if not openable.is_openable:
        print("That is not something you can do that to.")
        return

    key_found = check_key_for(openable)

    if key_found:
        if verb is Verb.UNLOCK:
            if not openable.is_locked:
                print("This is already unlocked.")
            else:
                openable.is_locked, openable.is_sealed = False, False
                print(f"You unlock {openable.name} with {key_found}.")

        if verb is Verb.LOCK:
            if openable.is_locked:
                print("This is already locked.")
            else:
                openable.is_locked, openable.is_sealed = True, True
                print(f"You lock {openable.name} with {key_found}.")
    else:
        print("You can't do that without the right key.")


def open_or_close_output(verb: Verb, openable) -> str:
    locked = openable.is_locked
    sealed = openable.is_sealed

    if locked and sealed:
        return "It is locked."

    if verb is Verb.OPEN:
        if sealed:
            openable.is_sealed = False
            return f"You open {openable.name}."
        else: return f"{openable.name.capitalize()} is already open."

    if verb is Verb.CLOSE:
        if not sealed:
            openable.is_sealed = True
            return f"You close {openable.name}."
        else: return f"{openable.name.capitalize()} is already closed."
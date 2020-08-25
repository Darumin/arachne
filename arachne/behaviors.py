from typing import Any
from functools import partial

from arachne.lingo import Object, Verb
from arachne.game import _Player, _Game
from arachne.nouns import Container
# the bulk of game behavior is found here


class Behavior:
    @staticmethod
    def return_attribute(given, attribute) -> str:
        """
        :param given: Noun
        :param attribute: str
        """
        return getattr(given, attribute)

    @staticmethod
    def set_start(room) -> None:
        """
        :param room: Room
        """
        _Game._start_location = room
        Behavior.set_player_location(room)

    @staticmethod
    def room_description(room) -> str:
        """
        :param room: Room
        """
        desc: str = return_name(room)
        desc += "\n" + return_examined(room)
        desc += Behavior.room_placed_description(room)
        return desc

    @staticmethod
    def room_placed_description(room) -> str:
        """
        :param room: Room
        """
        extra: dict = return_contents(room)
        desc: str = ""
        if extra:
            desc += "\n\n"
            for each in extra.values():
                if each.is_concealed is False:
                    desc += return_encountered(each) + " "
        return desc

    @staticmethod
    def _inventory_values():
        return _Player.contents.values()

    @staticmethod
    def _inventory_keys():
        return _Player.contents.keys()

    @staticmethod
    def _inventory_dict():
        return _Player.contents

    @staticmethod
    def check_inventory(item_str: str) -> bool:
        inv = dict(Behavior._inventory_dict())
        for item_id in inv:
            instance = inv[item_id]
            if item_str in instance.name:
                return True
        return False

    @staticmethod
    def add_to_inventory(item) -> None:
        """
        :param item: Item
        """
        Behavior.add_to_container(_Player, item)

    @staticmethod
    def free_item(item):
        """
        :param item: Item
        """
        parent = item.parent_container
        if parent:
            item.parent_container = None
            Behavior.remove_from_container(parent, item)

    @staticmethod
    def player_location():
        return _Player.current_location

    @staticmethod
    def set_player_location(room: Any):
        _Player.current_location = room

    @staticmethod
    def vicinity() -> dict:
        current_location = Behavior.player_location()
        inventory = Behavior._inventory_dict()
        return {**current_location.contents, **inventory}

    @staticmethod
    def add_to_container(container, item):
        """
        :param container: Room or Container
        :param item: Item
        """
        _key: int = id(item)
        if _key not in container.contents:
            container.contents[_key] = item
            item.parent_container = container

    @staticmethod
    def drop_in_room(item):
        """
        :param item: Item
        """
        item.when_encountered = f"{item.name.capitalize()} is here."
        room_dropped = Behavior.player_location()
        Behavior.add_to_container(room_dropped, item)

    @staticmethod
    def remove_from_container(container, item):
        """
        :param container: Container
        :param item: Item
        """
        container.contents.pop(id(item))

    @staticmethod
    def guess_object(object_str: str) -> tuple:
        """
        :return: tuple of (Object, list)
        """
        results: list = list()
        if object_str == "": return Object.UNSPECIFIED, results

        # check vicinity (everywhere except inventory) for closest matching subject
        vicinity: dict = Behavior.vicinity()
        for object_id in vicinity:
            instance = vicinity[object_id]
            if object_str in instance.name \
                    and not instance.is_concealed:
                results.append(instance)

        # check what kind of subject input this is
        typified = Behavior.typify_object(object_str, len(results))

        # if multiple matches, resolve the matches
        # if nonexistent, create a list with one entry for the sake of returning a valid tuple
        if typified is Object.MULTIPLE: return Behavior.resolve_multiple(results)
        if typified is Object.NONEXISTENT: results.append(Object.NONEXISTENT)

        # finally return this tuple if nothing else applies
        return typified, results[0]

    @staticmethod
    def typify_object(object_str: str, amount_found: int) -> Object:
        if object_str == "all": return Object.ALL
        if amount_found == 0: return Object.NONEXISTENT
        if amount_found > 1: return Object.MULTIPLE
        if Behavior.check_inventory(object_str): return Object.POSSESSED
        return Object.FOUND

    @staticmethod
    def resolve_multiple(results: list):
        print("Which one?")

        for result in enumerate(results, start=1):
            print(f"{result[0]})", result[1].name, end=" ")

        choice: str = input("\n>")
        return Behavior.guess_object(choice)

    @staticmethod
    def is_container(noun):
        return isinstance(noun, Container)

    @staticmethod
    def check_for_key(container: Container) -> bool:
        for each in Behavior._inventory_values():
            unlock_id = return_unlock_id(each)
            if unlock_id == id(container):
                return True
        return False

    @staticmethod
    def lock_outputs(verb: Verb, container: Container):
        if Behavior.is_container(container):
            key_found = Behavior.check_for_key(container)
            if key_found:
                if verb is Verb.UNLOCK:
                    if not container.is_sealed:
                        print("This is already unlocked.")
                        return
                    else:
                        container.is_sealed = False
                        print(f"{container.name.capitalize()} has been unlocked.")
                elif verb is Verb.LOCK:
                    if container.is_sealed:
                        print("This is already locked.")
                        return
                    else:
                        container.is_sealed = True
                        print(f"{container.name.capitalize()} has been locked.")
            else:
                print("You can't do that without a key.")
        else:
            print("That is not something you can do that to.")


return_name = partial(Behavior.return_attribute, attribute="name")
return_examined = partial(Behavior.return_attribute, attribute="when_examined")
return_contents = partial(Behavior.return_attribute, attribute="contents")
return_encountered = partial(Behavior.return_attribute, attribute="when_encountered")
return_unlock_id = partial(Behavior.return_attribute, attribute="unlock_id")

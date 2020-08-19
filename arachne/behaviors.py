from typing import Any
from functools import partial
from arachne.game import _Player, _Game
# the bulk of game behavior is found here


class Behavior:
    @staticmethod
    def return_attribute(given, attribute: str) -> str:
        """
        :param given: Noun
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
                desc += return_encountered(each) + " "
        return desc

    @staticmethod
    def inventory():
        return _Player.contents.values()

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
        _current_location: Any = Behavior.player_location()
        return _current_location.contents

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
    def remove_from_container(container, item):
        """
        :param container: Container
        :param item: Item
        """
        container.contents.pop(id(item))


return_name = partial(Behavior.return_attribute, attribute="name")
return_examined = partial(Behavior.return_attribute, attribute="when_examined")
return_contents = partial(Behavior.return_attribute, attribute="contents")
return_encountered = partial(Behavior.return_attribute, attribute="when_encountered")

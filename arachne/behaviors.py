from typing import Any
from functools import partial
from arachne.game import _Player, _Game


class Behavior:
    @staticmethod
    def set_start(room: Any):
        _Game._start_location = room
        Behavior.set_player_location(room)

    @staticmethod
    def return_attribute(given: Any, attribute: str) -> str:
        return getattr(given, attribute)

    @staticmethod
    def room_description(given: Any) -> str:
        desc: str = return_name(given)
        desc += "\n" + return_examined(given)
        desc += Behavior.room_placed_description(given)
        return desc

    @staticmethod
    def room_placed_description(given: Any) -> str:
        extra: dict = return_contents(given)
        desc: str = ""
        if extra:
            desc += "\n\n"
            for each in extra.values():
                desc += return_encountered(each) + " "
        return desc

    @staticmethod
    def add_to_inventory(item: Any):
        Behavior.add_to_container(_Player, item)

    @staticmethod
    def inventory():
        return _Player.contents

    @staticmethod
    def free_item(item: Any):
        _contents = item
        if _contents:
            Behavior.remove_from_container(_contents, item)
            item.parent_container = None

    @staticmethod
    def player_location():
        return _Player.current_location

    @staticmethod
    def set_player_location(room: Any):
        _Player.current_location = room

    @staticmethod
    def add_to_container(given: Any, item: Any):
        given.contents = Behavior._add_to_container(given, item)

    @staticmethod
    def _add_to_container(given: Any, item: Any) -> dict:
        _contents: dict = return_contents(given)
        _key: int = id(item)
        if _key not in _contents:
            _contents[_key] = item
        return dict(_contents)

    @staticmethod
    def remove_from_container(given: Any, item: Any):
        given.contents.pop(id(item))


return_name = partial(Behavior.return_attribute, attribute="name")
return_examined = partial(Behavior.return_attribute, attribute="when_examined")
return_contents = partial(Behavior.return_attribute, attribute="contents")
return_encountered = partial(Behavior.return_attribute, attribute="when_encountered")
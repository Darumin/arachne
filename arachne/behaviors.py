from typing import Any
from functools import partial


class Behavior:
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
        extra = return_contents(given)
        desc = ""
        if extra:
            desc += "\n\n"
            for each in extra.values():
                desc += return_encountered(each) + " "
        return desc

    @staticmethod
    def add_to_container(given: Any, item: Any):
        given.contents = Behavior._add_to_container(given, item)

    @staticmethod
    def _add_to_container(given: Any, item: Any) -> dict:
        _contents = return_contents(given)
        _key = id(item)
        if _key not in _contents:
            _contents[_key] = item
        return dict(_contents)


return_name = partial(Behavior.return_attribute, attribute="name")
return_examined = partial(Behavior.return_attribute, attribute="when_examined")
return_contents = partial(Behavior.return_attribute, attribute="contents")
return_encountered = partial(Behavior.return_attribute, attribute="when_encountered")
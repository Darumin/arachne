from dataclasses import dataclass, field
from typing import Any
# all the nouns in Arachne are found here


@dataclass
class Noun:
    """
    PARAMETERS

    name: Try to initialize with articles, i.e. "the yellow onion" for more natural English printing. Required.
    when_examined: Description that prints when examine action is used. Required.
    when_encountered: Description when first encountered in a room or a container.
    is_concealed: Defaults to False. When things are hidden from view, as in inside a closed container,
    and extra action must be taken to uncover them, i.e. opening a container.
    is_sealed: Defaults to False. Initialize with True to create a locked item. Sealed can only be
    opened with appropriate keys. Can apply to things like doors and containers, but this behavior
    can be extended to unlikely nouns.
    """
    name: str
    when_examined: str
    when_encountered: str = ""
    when_opened: str = ""
    is_concealed: bool = False
    is_sealed: bool = False


@dataclass
class Container(Noun):
    contents: dict = field(default_factory=dict)


@dataclass
class Room(Container):
    # adjacency
    pass


@dataclass
class Item(Noun):
    parent_container: Any = None
    gettable: bool = False

    def __repr__(self):
        return f"<item:'{self.name}'-> {id(self)}>"


@dataclass
class Key(Item):
    unlock_id: int = 0


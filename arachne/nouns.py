from dataclasses import dataclass, field
from typing import Any
# all the nouns in Arachne are found here


@dataclass
class Noun:
    name: str
    when_examined: str
    when_encountered: str = ""
    is_gettable: bool = False
    is_concealed: bool = False
    is_sealed: bool = False

    @property
    def has_contents(self):
        return True if isinstance(self, Container) else False


@dataclass
class Container(Noun):
    contents: dict = field(default_factory=dict)

    def __repr__(self):
        return f"<container:'{self.name}'-> {id(self)}>"


@dataclass
class Room(Container):
    # adjacency
    pass


@dataclass
class Item(Noun):
    parent_container: Any = None

    def __repr__(self):
        return f"<item:'{self.name}'-> {id(self)}>"


@dataclass
class Key(Item):
    unlock_id: int = 0


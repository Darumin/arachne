from dataclasses import dataclass, field
from typing import Any
# all the nouns in Arachne are found here



@dataclass
class Noun:
    name: str
    when_examined: str = ""
    when_encountered: str = ""
    is_locked: bool = False
    is_concealed: bool = False
    is_sealed: bool = False

    @property
    def is_openable(self):
        temp = (Container(name=""), Door(name=""))
        _temp = [i.__class__ for i in temp]
        return self.__class__ is temp.__class__

    @property
    def is_gettable(self):
        temp = (Item(name=""), Key(name=""))
        _temp = [i.__class__ for i in temp]
        return self.__class__ in _temp

    @property
    def has_contents(self):
        return isinstance(self, Container)


@dataclass
class Container(Noun):
    contents: dict = field(default_factory=dict)

    def __repr__(self):
        return f"<container:'{self.name}'-> {id(self)}>"


@dataclass
class Room(Container):
    adjacency: dict = field(default_factory=dict)

    def __repr__(self):
        return f"<room:'{self.name}'-> {id(self)}>"


@dataclass
class Item(Noun):
    parent_container: Any = None

    def __repr__(self):
        return f"<item:'{self.name}'-> {id(self)}>"


@dataclass
class Key(Item):
    unlock_id: int = 0

    def __repr__(self):
        return f"<key:'{self.name}'-> {id(self)}>"


@dataclass
class Door(Noun):
    portal_id: int = 0

    def __repr__(self):
        return f"<door:'{self.name}'-> {id(self)}>"

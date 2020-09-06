from dataclasses import dataclass, field
from typing import Any


@dataclass
class Noun:
    name: str
    when_examined: str = ''
    when_encountered: str = ''
    is_locked: bool = False
    is_concealed: bool = False
    is_sealed: bool = False

    def __str__(self):
        return '<%s -> %i>' % (self.__class__.__name__, id(self))

    @property
    def is_openable(self):
        temp = self.__class__.__name__
        return temp is 'Container' or temp is 'Door'

    @property
    def is_gettable(self):
        temp = self.__class__.__name__
        return temp is 'Item' or temp is 'Key'


@dataclass
class GameInfo:
    game_title: str
    byline: str
    preface: str
    start: Any


@dataclass
class Container(Noun):
    contents: dict = field(default_factory=dict)


@dataclass
class Room(Container):
    adjacency: dict = field(default_factory=dict)


@dataclass
class Item(Noun):
    parent_container: Any = None


@dataclass
class Key(Item):
    key_to: Any = None


@dataclass
class Door(Noun):
    room_context: dict = field(default_factory=dict)

    @property
    def is_maxed(self):
        return False if len(self.room_context) < 2 else True

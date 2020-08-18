from dataclasses import dataclass, field
from typing import Any
# all the nouns in Arachne are found here


@dataclass
class Noun:
    name: str
    when_examined: str
    when_encountered: str = ""


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

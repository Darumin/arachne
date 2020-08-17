from dataclasses import dataclass, field
from typing import Any


@dataclass
class Noun:
    name: str
    when_examined: str
    when_encountered: str = ""

@dataclass
class Room(Noun):
    contents: dict = field(default_factory=dict)

@dataclass
class Item(Noun):
    parent_container: Any = None
    gettable: bool = False


from typing import Any
# the primary game state hub


class Game(object):
    __instance = None

    def __new__(cls, start):
        if Game.__instance is None:
            Game.__instance = object.__new__(cls)
        Game.__instance.start = start
        return Game.__instance

    def __repr__(self):
        return f"<GAME: {id(self)}, START: '{self.start}'>"


class _Player:
    current_location: Any = None
    contents: dict = dict()

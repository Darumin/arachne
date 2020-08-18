# The primary game state hub. Single instance classes.
from typing import Any


class _Game:
    _start_location = None


class _Player:
    current_location: Any = None
    contents: dict = dict()

    @staticmethod
    def vicinity():
        return _Player.current_location.contents

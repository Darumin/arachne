from typing import Any
# the primary game state hub


class _Game:
    _start_location = None


class _Player:
    current_location: Any = None
    contents: dict = dict()

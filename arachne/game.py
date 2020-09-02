from typing import Any
# the primary game state hub


class Game:
    class _Game:
        def __init__(self, start):
            self.start_location = start
    instance = None

    def __init__(self, arg):
        if not Game.instance:
            Game.instance = Game._Game(arg)
        else:
            Game.instance.start_location = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


class _Player:
    current_location: Any = None
    contents: dict = dict()

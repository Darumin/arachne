# The primary game state hub.

class Game:
    # TODO: When I finally do the main game loop, this should be initialized as beginning room.
    _start_location = None
    _noun_ids: list = []


    @property
    def start(self) -> _start_location:
        return self._start_location

    @staticmethod
    def ids() -> list:
        return Game._noun_ids

    @staticmethod
    def add_noun(noun):
        # Type hint: noun is type Noun.
        Game._noun_ids.append(noun)

    @staticmethod
    def set_start(room):
        Game._start_location = room

    @staticmethod
    def set_location(room):
        Game._player_location = room

    @staticmethod
    def validate_location() -> bool:
        return Game._start_location in Game.ids
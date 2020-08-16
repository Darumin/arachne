# The primary game state hub.

class Game:
    # TODO: When I finally do the main game loop, this should be initialized as beginning room.
    _start_location = None
    _noun_ids = []

    @staticmethod
    def add_noun(noun):
        # Type hint: noun is type Noun.
        Game._noun_ids.append(noun)

    @staticmethod
    def get_objects() -> list:
        return Game._noun_ids

    @staticmethod
    def set_location(given_id: str):
        Game._player_location = given_id

    @staticmethod
    def get_location() -> _start_location:
        return Game._start_location

    @staticmethod
    def validate_location() -> bool:
        return Game._start_location in Game.get_objects()
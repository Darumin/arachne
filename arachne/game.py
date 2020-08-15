from arachne.nouns import Noun


class Game:
    # TODO: When I finally do the main game loop, this should be initialized as beginning room.
    _player_location = None

    @staticmethod
    def set_location(given_id: str):
        Game._player_location = given_id

    @staticmethod
    def get_location() -> _player_location:
        return Game._player_location

    @staticmethod
    def validate_location() -> bool:
        return Game._player_location in Noun.get_objects()
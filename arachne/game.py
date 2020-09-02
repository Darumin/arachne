class Game(object):
    __instance = None

    def __new__(cls, game_title, byline, preface, start):
        if Game.__instance is None:
            Game.__instance = object.__new__(cls)

        Game.__instance.game_title = game_title
        Game.__instance.byline = byline
        Game.__instance.preface = preface
        Game.__instance.start = start

        return Game.__instance

    def __repr__(self):
        return f"<GAME: {id(self)}, START: '{self.start}'>"


class Player:
    current_location = None
    contents: dict = dict()

from app import Noun


class Player(Noun):
    def __init__(self, name):
        super().__init__(name)
        # TODO: Implement basic location tracking, verbs, noun behaviors
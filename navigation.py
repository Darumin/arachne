from app import Noun


class Player(Noun):
    def __init__(self, true_name: str, description: str):
        super().__init__(true_name, description)
        # TODO: Implement basic location tracking, verbs, noun behaviors
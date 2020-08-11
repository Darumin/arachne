# This is the reference for all actions in the game. Arachne actions are
# defined according to a single input/output architecture.

from arachne.nouns import Noun


class Player(Noun):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        # TODO: Clean up actions
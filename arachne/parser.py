from arachne.game import Game as g
from arachne.verbs import Verb


def write_action(action: Verb) -> None:
    if action is Verb.TAKE: Parser.take()
    if action is Verb.EXAMINE: pass


class Parser:
    @staticmethod
    def take():
        pass

    @staticmethod
    def scan_vicinity():
        loc = g.get_location()
        return loc

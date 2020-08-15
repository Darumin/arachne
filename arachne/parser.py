# TODO: Scan vicinity must check all location's contents + free items and items in
# TODO: open containers

from arachne.lexer import tokenize
from arachne.game import Game as g
from arachne.verbs import Verb


def write_action(input_str: str) -> None:
    lowered = input_str.lower()
    verb, subject = tokenize(lowered)

    if verb is Verb.TAKE: print(Parser.take(subject))
    if verb is Verb.EXAMINE: pass
    if verb is Verb.NULL: print(Parser.lecture_player())


class Parser:
    @staticmethod
    def take(subject_str: str):
        if not subject_str:
            return "No such subject."
        return f"You take the {subject_str}"

    @staticmethod
    def scan_vicinity():
        loc = g.get_location()
        return loc

    @staticmethod
    def lecture_player() -> str:
        return "That is not a good input."

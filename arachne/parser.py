# TODO: Scan vicinity must check all location's contents + free items and items in
# TODO: open containers

from arachne.lexer import tokenize
from arachne.game import Game as g
from arachne.verbs import Verb
from arachne.nouns import Player, Item


def write_action(input_str: str) -> None:
    lowered = input_str.lower()
    verb, subject = tokenize(lowered)

    if verb is Verb.TAKE: print(Parser.take(subject))
    if verb is Verb.EXAMINE: pass
    if verb is Verb.NULL: print(Parser.lecture_player())


class Parser:
    @staticmethod
    def take(subject_pair: tuple) -> str:
        header, subject = subject_pair
        if header is False:
            return f"This isn't available -> '{subject}'"
        if subject in Player.get_ids():
            return f"{subject.name} is already in your posession."

        Player.store(subject)
        print(Player.inventory())
        return f"You take the {subject.name}."

    @staticmethod
    def scan_vicinity():
        loc = g.get_location()
        return loc

    @staticmethod
    def lecture_player() -> str:
        return "That is not a good input."

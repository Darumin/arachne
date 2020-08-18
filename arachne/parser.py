# TODO: Work on freeing items from their parent containers.
from arachne.lexer import tokenize
from arachne.lingo import Verb
from arachne.behaviors import Behavior as be
# this is where input is parsed from passed tokens, then resolves into turn event


# this function writes the resulting action of given input!
def write_action(input_str: str) -> None:
    # verb is type str, subject is type tuple
    lowered: str = input_str.lower()
    verb, subject = tokenize(lowered)

    if verb is Verb.LOOK: print(Parser.look())
    if verb is Verb.TAKE: print(Parser.take(subject))
    if verb is Verb.EXAMINE: pass
    if verb is Verb.NULL: print(Parser.lecture_player())


class Parser:
    @staticmethod
    def look() -> str:
        return be.room_description(be.player_location())

    @staticmethod
    def take(subject_pair: tuple) -> str:
        header, subject = subject_pair

        # TODO: somehow refactor this into something less ugly
        if not subject:
            # TODO: far future, please add implicit taking, i.e. "take {last_interacted}"
            return "Please specify what you want to take."
        if header is False:
            return f"This isn't available -> '{subject}'"
        if subject in be.inventory():
            return f"{subject.name.capitalize()} is already in your posession."

        be.add_to_inventory(subject)
        # be.free_item(subject)
        return f"You take {subject.name}."

    @staticmethod
    def lecture_player() -> str:
        return "That is not a good input."

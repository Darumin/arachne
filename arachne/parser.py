from arachne.lexer import tokenize
from arachne.lingo import Verb, Subject
from arachne.behaviors import Behavior as be
# this is where input is parsed from passed tokens, then resolves into turn event


# this function writes the resulting action of given input!
def write_action(input_str: str) -> None:
    # verb is type str, subject is type tuple
    lowered: str = input_str.lower()
    verb, subject_pair = tokenize(lowered)

    if verb is Verb.LOOK: print(Parser.look())
    if verb is Verb.TAKE: print(Parser.take(subject_pair))
    if verb is Verb.DROP: pass
    if verb is Verb.EXAMINE: print(Parser.examine(subject_pair))
    if verb is Verb.PUT: pass
    if verb is Verb.INVENTORY: pass
    if verb is Verb.USE: pass

    if verb is Verb.NULL: print(Parser.lecture_player())


class Parser:
    @staticmethod
    def look() -> str:
        return be.room_description(be.player_location())

    @staticmethod
    def take(subject_pair: tuple) -> str:
        """
        :param subject_pair: tuple of Subject, Item
        """
        subject, result = subject_pair

        # TODO: far future, please add implicit taking, i.e. "take {last_interacted}"
        if subject is Subject.UNSPECIFIED: return "What do you want to take?"
        if subject is Subject.NONEXISTENT: return f"This isn't available -> '{result}'"
        if result in be.inventory(): return f"{subject.name.capitalize()} is already in your posession."

        be.free_item(result)
        be.add_to_inventory(result)

        return f"You take {result.name}."

    @staticmethod
    def examine(subject_pair: tuple) -> str:
        """
        :param subject_pair: tuple of Subject, Item
        """
        subject, result = subject_pair

        if subject is Subject.UNSPECIFIED: return "What do you want to look at?"
        if subject is Subject.NONEXISTENT: return f"You can't examine that -> '{result}'"

        return f"{result.when_examined}"

    @staticmethod
    def lecture_player() -> str:
        return "That is not a good input."

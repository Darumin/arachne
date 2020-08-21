# TODO: consolidate "guess object" behavior
from arachne.lexer import tokenize
from arachne.lingo import Verb, Object
from arachne.behaviors import Behavior as be
# this is where input is parsed from passed tokens, then resolves into turn event


# this function writes the resulting action of given input!
def write_action(input_str: str) -> None:
    results = []
    lowered: str = input_str.lower()
    tokenize(lowered, results)
    verb = results[0][0]

    if verb is Verb.LOOK: return Parser.look()
    if verb is Verb.TAKE: return Parser.take(results)
    if verb is Verb.DROP: return Parser.drop(results)
    if verb is Verb.EXAMINE: pass
    if verb is Verb.PUT: pass
    if verb is Verb.INVENTORY: pass
    if verb is Verb.USE: pass

    return Parser.lecture_player()


class Parser:
    @staticmethod
    def look() -> None:
        print(be.room_description(be.player_location()))

    @staticmethod
    def take(results: list) -> None:
        given_obj = ""

        # we only want to identify one object and ignore everything else
        for each in results:
            if isinstance(each[0], Object):
                given_obj = each[1]
                break

        # see if this object is valid
        # target is type Object, list_found is type list with first element type Item
        target, list_found = be.guess_object(given_obj)

        if target is Object.POSSESSED: print(f"You're carrying that -> {list_found[0].name}")
        elif target is Object.UNSPECIFIED: print("Please specify what you want to take.")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}'")
        elif target is Object.FOUND:
            be.free_item(list_found[0])
            be.add_to_inventory(list_found[0])
            print(f"You take {list_found[0].name.lower()}.")

    @staticmethod
    def drop(results: list):
        given_obj = ""

        for each in results:
            if isinstance(each[0], Object):
                given_obj = each[1]
                break

        target, list_found = be.guess_object(given_obj)

        if target is Object.UNSPECIFIED: print("Please specify what you want to drop.")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}")
        elif target is Object.FOUND: print(f"You are not carrying this -> '{given_obj}")
        elif target is Object.POSSESSED:
            be.free_item(list_found[0])
            be.drop_in_room(list_found[0])
            print(f"You drop {list_found[0].name.lower()}.")

    @staticmethod
    def examine(results: list) -> None:
        pass

    @staticmethod
    def lecture_player() -> None:
        print("That is not a good input.")

# TODO: Need to implement OPEN and CLOSE
from arachne.lexer import tokenize
from arachne.lingo import Verb, Object, Prep, Compass
from arachne.behaviors import Behavior as be
# this is where input is parsed from passed tokens, then resolves into turn event


# this function writes the resulting action of given input!
def write_action(input_str: str) -> None:
    results = []
    lowered: str = input_str.lower()
    tokenize(lowered, results)
    verb = results[0][0]

    if isinstance(verb, Compass):
        print("GO")
        return

    if verb is Verb.LOOK: return Parser.look()
    if verb is Verb.TAKE: return Parser.take(results)
    if verb is Verb.DROP: return Parser.drop(results)
    if verb is Verb.EXAMINE: return Parser.examine(results)
    if verb is Verb.PUT: return Parser.put(results)
    if verb is Verb.INVENTORY: return Parser.inventory()

    if verb is Verb.UNLOCK or verb is Verb.LOCK: return Parser.lock_switch(verb, results)
    if verb is Verb.OPEN or verb is Verb.CLOSE: pass

    return Parser.lecture_player()


class Parser:
    @staticmethod
    def look() -> None:
        print(be.room_description(be.player_location()))

    @staticmethod
    def take(results: list) -> None:
        # we only want to identify one object and ignore everything else. from that identification
        # derive a target of type Object, and an obj of type Item.
        given_obj = Parser._get_obj_str(results)
        target, obj = be.guess_object(given_obj)

        if target is Object.POSSESSED: print(f"You're carrying that -> '{obj.name}'")
        elif target is Object.UNSPECIFIED: print("Please specify what you want to take, i.e. \"take the crown\"")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}'")
        elif target is Object.FOUND:
            if obj.is_gettable:
                be.free_item(obj)
                be.add_to_inventory(obj)
                print(f"You take {obj.name.lower()}.")
            else: print(f"That can't be taken. -> {obj.name}")

    @staticmethod
    def drop(results: list):
        given_obj = Parser._get_obj_str(results)
        target, obj = be.guess_object(given_obj)

        if target is Object.UNSPECIFIED: print("Please specify what you want to drop, i.e. \"drop the mic\"")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}'")
        elif target is Object.FOUND: print(f"You are not carrying this -> '{given_obj}'")
        elif target is Object.POSSESSED:
            be.free_item(obj)
            be.drop_in_room(obj)
            print(f"You drop {obj.name.lower()}.")

    @staticmethod
    def examine(results: list) -> None:
        given_obj = Parser._get_obj_str(results)
        target, obj = be.guess_object(given_obj)

        if target is Object.UNSPECIFIED: print("Please specify what you want to examine, i.e. \"examine dog\"")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}'")
        elif target is Object.FOUND or target is Object.POSSESSED:
            description = obj.when_examined
            if obj.has_contents:
                description += be.describe_contents(obj)
            print(description)

    @staticmethod
    def lock_switch(verb: Verb, results: list):
        given_obj = Parser._get_obj_str(results)
        target, obj = be.guess_object(given_obj)

        if target is Object.UNSPECIFIED: print("What do you want to do that to?")
        elif target is Object.NONEXISTENT: print(f"This isn't available -> '{given_obj}'")
        elif target is Object.FOUND or target is Object.POSSESSED:
            be.lock_outputs(verb, obj)

    @staticmethod
    def put(results: list):
        obj_list, preposition = Parser._extend_with_prep(results)
        if not obj_list or not preposition:
            print("Please specify what you want to do, i.e. \"put coin in box\"")
            return

        if len(obj_list) == 1:
            print(f"{obj_list[0][1].capitalize()} {preposition[0][1]} what?")
            return

        target_one, obj_one = be.guess_object(obj_list[0][1])
        target_two, obj_two = be.guess_object(obj_list[1][1])

        if obj_one is Object.NONEXISTENT or obj_two is Object.NONEXISTENT:
            print("There is no such thing.")
            return

        if preposition[0][0] is Prep.WITHIN:
            if obj_one.is_gettable:
                be.free_item(obj_one)
                be.add_to_container(obj_two, obj_one)
                print(f"You put {obj_one.name} in {obj_two.name}.")
            else:
                print("That can't be stored.")

    @staticmethod
    def inventory():
        print(be.describe_inventory())

    @staticmethod
    def lecture_player() -> None:
        print("That is not a good input.")

    @staticmethod
    def _get_obj_str(results: list) -> str:
        given_obj = ""

        for each in results:
            if isinstance(each[0], Object):
                given_obj = each[1]
        return given_obj

    @staticmethod
    def _extend_with_prep(results: list) -> tuple:
        extends, prep = list(), list()

        for each in results:
            if isinstance(each[0], Object):
                extends.append(each)
            elif isinstance(each[0], Prep):
                prep.append(each)

        return extends, prep

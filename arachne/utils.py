from gc import get_objects
from collections import Counter
from arachne.lingo import nouns


# returns a list of all active instances
def print_all_instances() -> None:
    counted_objects: Counter = _count_objects()

    print("ALL ACTIVE")
    for obj in counted_objects:
        print(f"{obj}s: {counted_objects[obj]}")


def _count_objects() -> Counter:
    obj_list: list = [
        # get all active instances of noun objects
        str(type(o).__name__)
        for o in get_objects()
        if _valid_noun(o)
    ]

    _count = Counter()
    for obj in obj_list:
        _count[obj] += 1

    return _count


def _valid_noun(obj) -> bool:
    for noun in nouns:
        if isinstance(obj, noun):
            return True
    return False

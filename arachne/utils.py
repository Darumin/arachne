import gc
from collections import Counter
from arachne.nouns import Container, Item, Door, Room, Key

_noun_index = (Container, Item, Door, Room, Key)


# returns a list of all active instances of `object_type`
def print_all_instances():
    counted_objects = _count_objects()

    print("ALL ACTIVE")
    for obj in counted_objects:
        print(f"{obj}s: {counted_objects[obj]}")


def _count_objects() -> Counter:
    obj_list = [
        # get all active instances of noun objects
        str(type(o).__name__)
        for o in gc.get_objects()
        if _valid_noun(o)
    ]

    _count = Counter()
    for obj in obj_list:
        _count[obj] += 1

    return _count


def _valid_noun(obj) -> bool:
    for noun in _noun_index:
        if isinstance(obj, noun):
            return True
    return False

from gc import get_objects
from collections import Counter
from arachne.lingo import nouns


# returns a count of all active instances
def count_all_instances() -> Counter:
    obj_list: list = [
        str(type(o).__name__)
        for o in get_objects()
        if o.__class__ in nouns
    ]

    counted_instances: Counter = Counter()
    for obj in obj_list:
        counted_instances[obj] += 1

    return counted_instances

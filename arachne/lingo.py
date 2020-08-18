from enum import Enum
# constants subclassing enum


class Verb(Enum):
    # basic player actions
    LOOK = "takes in surroundings"
    TAKE = "takes either a single item or all"
    DROP = "move designated item to floor"
    EXAMINE = "returns description of object"
    PUT = "move designated item to container"
    INVENTORY = "inspects player's possessions"
    USE = "uses designated item"

    # room limitation actions
    OPEN = ''
    CLOSE = ''
    LOCK = ''
    UNLOCK = ''

    # social and personal actions
    THINK = "can be used as an objective tracker"
    ASK = ''
    TELL = ''
    SAY = ''
    GIVE = ''
    SHOW = ''

    # sequence actions
    WAIT = ''
    REPEAT = ''

    # case of bad verb
    NULL = "invalid input"

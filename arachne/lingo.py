from enum import Enum

##
### Arachne's enum vocabulary.
##


class Verb(Enum):
    LOOK = "takes in surroundings"
    TAKE = "takes either a single item or all"
    DROP = "move designated item to floor"
    EXAMINE = "returns description of object"
    PUT = "move designated item to container"
    INVENTORY = "inspects player's possessions"
    USE = "uses designated item"

    OPEN = ''
    CLOSE = ''
    LOCK = ''
    UNLOCK = ''

    THINK = "can be used as an objective tracker"
    ASK = ''
    TELL = ''
    SAY = ''
    GIVE = ''
    SHOW = ''

    WAIT = ''
    REPEAT = ''

    NULL = 'invalid input'
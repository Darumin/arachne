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


class Desc(Enum):
    SELF = "default description; refers to itself"
    PLACEMENT = "initial description of noun when staged in a setting by author"
    DROPPED = "description when outside of inventory, has default"
    STORED = "description of an item in a container"

from enum import Enum

##
### This is a list of Arachne's default verbs.
##


class Verb(Enum):
    TAKE = 'takes either a single item or all'
    DROP = 'move designated item to floor'
    EXAMINE = 'returns description of object'
    PUT = 'move designated item to container'
    INVENTORY = 'inspects self'

    OPEN = ''
    CLOSE = ''
    LOCK = ''
    UNLOCK = ''

    ASK = ''
    TELL = ''
    SAY = ''
    GIVE = ''
    SHOW = ''

    WAIT = ''
    REPEAT = ''

    NULL = 'invalid input'

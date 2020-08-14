from enum import Enum

"""
This is a list of Arachne's default verbs.

"Verb" is a container using class syntax and subclasses Enum.
The resulting Verb-type constants are used for equality checks and 
guarding against errors in noun interaction. The string values are 
unused and serve primarily as documentation.
"""


class Verb(Enum):
    TAKE = 'takes either a single item or all'
    EXAMINE = 'returns description of object'
    DROP = 'move designated item to floor'
    STORE = 'move designated item to container'
    INVENTORY = 'inspects self'

    NULL = 'invalid input'

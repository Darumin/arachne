"""
This is a list of all verbs in a given game.

Verb is a container class that inherits from Enum, which renders these as constants of type Verb.
The values are unused and serve as a form of documentation. Constants are used in equality checks.
"""

from enum import Enum


class Verb(Enum):
    TAKE = 'takes either a single item or all'
    EXAMINE = 'returns description of object'
    DROP = 'move designated item to floor'
    STORE = 'move designated item to container'
    INVENTORY = 'inspects self'

    NULL = 'invalid input'

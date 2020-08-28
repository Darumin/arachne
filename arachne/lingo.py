from enum import Enum
# constants subclassing enum


class Verb(Enum):
    # basic player actions
    LOOK = "i'm rotating it in my mind"
    TAKE = "the act of picking things up"
    DROP = "the act of putting things down"
    PUT = "the act of placing things where you want them"
    EXAMINE = "when you want to really see something"
    INVENTORY = "when you really want to see your somethings"
    USE = "when you want to spend your somethings"

    # room limitation actions
    OPEN = "open a container or door"
    CLOSE = "close a container or door"
    UNLOCK = "unlock a container or door"
    LOCK = "lock a container or door"

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


class Object(Enum):
    FOUND = "there's something like that nearby"
    MULTIPLE = "there's more than one thing like that nearby"
    NONEXISTENT = "there's nothing like that nearby"
    UNSPECIFIED = "there's nothing"
    POSSESSED = "not in a scary sense, but in a carry sense"

    ALL = "every loose item nearby"


class Prep(Enum):
    WITHIN = "put the toy in the box"
    ATOP = "place the toy on the box"
    SETTING = "turn the dial to ten"

    NONE = "no prep specified"


class Compass(Enum):
    NORTH = "north"
    EAST = "east"
    WEST = "west"
    SOUTH = "south"

    NORTHEAST = "northeast"
    NORTHWEST = "northwest"
    SOUTHEAST = "southeast"
    SOUTHWEST = "southwest"

    UP = "going up"
    DOWN = "coming down"

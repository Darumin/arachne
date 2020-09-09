from enum import Enum
import arachne.nouns as a


nouns = (
    a.Container,
    a.Item,
    a.Door,
    a.Room,
    a.Key,
    a.Door
)


class Verb(Enum):
    # basic player actions
    LOOK = 'im rotating it in my mind'
    TAKE = 'the act of picking things up'
    DROP = 'the act of putting things down'
    PUT = 'the act of placing things where you want them'
    EXAMINE = 'when you want to really see something'
    INVENTORY = 'when you really want to see your somethings'
    USE = 'when you want to spend your somethings'

    # room limitation actions
    OPEN = 'open a container or door'
    CLOSE = 'close a container or door'
    UNLOCK = 'unlock a container or door'
    LOCK = 'lock a container or door'

    # social and personal actions
    THINK = 'can be used as an objective tracker'
    ASK = ''
    TELL = ''
    SAY = ''
    GIVE = ''
    SHOW = ''

    # sequence actions
    WAIT = ''
    REPEAT = ''

    # case of bad verb
    NULL = 'invalid input'


# this is an arachne object, in the english grammar sense.
# not to be confused with object types.
class Object(Enum):
    FOUND = 'there is something like that nearby'
    MULTIPLE = 'there is more than one thing like that nearby'
    NONEXISTENT = 'there is nothing like that nearby'
    UNSPECIFIED = 'there is nothing'
    POSSESSED = 'not in a scary sense, but in a carry sense'

    ALL = 'every loose item nearby'


class Prep(Enum):
    WITHIN = 'put the toy in the box'
    ATOP = 'place the toy on the box'
    SETTING = 'turn the dial to ten'

    NONE = 'no prep specified'


class Compass(Enum):
    NORTH = 'north'
    EAST = 'east'
    WEST = 'west'
    SOUTH = 'south'

    NORTHEAST = 'northeast'
    NORTHWEST = 'northwest'
    SOUTHEAST = 'southeast'
    SOUTHWEST = 'southwest'

    UP = 'going up'
    DOWN = 'coming down'


# encompasses all known in-game vocabulary, unmatched vocab always default to type Object
lexicon = (
    ('ARTICLES', '^the$|^a$|^an$|^some$'),

    (Compass.NORTH, '^north$|^n$'),
    (Compass.EAST, '^east$|^e$'),
    (Compass.WEST, '^west$|^w$'),
    (Compass.SOUTH, '^south$|^s$'),

    (Compass.NORTHEAST, '^northeast$|^ne$'),
    (Compass.NORTHWEST, '^northwest$|^nw$'),
    (Compass.SOUTHEAST, '^southeast$|^se$'),
    (Compass.SOUTHWEST, '^southwest$|^sw$'),

    (Compass.UP, '^up$|^u$'),
    (Compass.DOWN, '^down$|^d$'),

    (Verb.LOOK, '^look$'),
    (Verb.TAKE, '^take$|^get$'),
    (Verb.DROP, '^drop$'),
    (Verb.PUT, '^put$|^store$|^place$'),
    (Verb.EXAMINE, '^x$|^check$|^examine$'),
    (Verb.INVENTORY, '^i$|^inv$|^inventory$'),
    (Verb.USE, '^use$|^consume$|^spend$'),

    (Verb.OPEN, '^open$'),
    (Verb.CLOSE, '^close$'),
    (Verb.UNLOCK, '^unlock$'),
    (Verb.LOCK, '^lock$'),

    (Prep.WITHIN, '^in$|^inside$|^into$'),
    (Prep.ATOP, '^on$|^above$'),
    (Prep.SETTING, '^at$|^to$')
)

from arachne.lingo import Verb
from arachne.game import _Game, _Player
import re


# This tuple of tuples displays acceptable synonym regexes of each default action verb.
verb_lexicon = (
    (Verb.LOOK,      "^look$"),
    (Verb.TAKE,      "^take$|^get$|^pick up$"),
    (Verb.DROP,      "^drop$"),
    (Verb.EXAMINE,   "^x$|^check$|^examine$"),
    (Verb.PUT,       "^put$|^store$"),
    (Verb.INVENTORY, "^i$|^inventory$|^inv$")
)


# Tokenizing function, parts out input into verb and subject fields.
def tokenize(given_str: str):
    a, b = _split_keywords(given_str)
    verb = _determine_verb(a)
    subject = _determine_subject(b)
    return verb, subject


#
##
### Following are private functions in the Pythonic sense.
##
#


# If input is a lone verb, no subject flag is raised
# and the case for lone verbs is passed.
def _split_keywords(given_str: str) -> tuple:
    split_input = given_str.split(' ', 1)

    if len(split_input) == 1:
        a = str(split_input[0])
        b = ""
        return a, b
    return tuple(split_input)


# Searches for pattern in verb, returns NULL keyword if unrecognized.
# If recognized, returns "head" of the Verb object, Regex tuple.
def _determine_verb(given_verb: str) -> Verb:
    for entry in verb_lexicon:
        match = re.search(entry[1], given_verb)
        if match:
            return entry[0]
    return Verb.NULL


def _determine_subject(given_subject: str = None) -> tuple:
    # TODO: trim articles here, refactor rename given_subject
    subject: str = _trim_article(given_subject)
    results: list = list()

    # in the case that a lone verb is inputted
    if subject == "": return True, None

    # TODO: In the future, check only in vicinity, not in all IDs.
    vicinity = _Player.vicinity()
    for object_id in vicinity:
        if subject in vicinity[object_id].name:
            results.append(object_id)

    if len(results) == 0:
        # in the case that no such string can be matched; subject doesn't exist
        return False, subject

    if len(results) > 1:
        # in the case that more than one item that matches given_subject, process all matches
        return _duplicates_resolution(results, subject)

    # finally return found object
    return True, vicinity[results[0]]


def _trim_article(given_str: str) -> str:
    # Did you know? That articles are actually adjectives;
    # they describe the nouns they precede.
    articles = "a|an|the|some"
    matched = re.match(articles, given_str)
    if matched:
        index = matched.end()
        return _trim_article(given_str[index + 1:])

    return given_str


def _duplicates_resolution(results: list, subject: str) -> tuple:

    print("Which one?")

    for result in enumerate(results, start=1):
        print(f"{result[0]})", result[1], end=" ")

    choice = input("\n>")
    return _determine_subject(choice)

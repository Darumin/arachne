# TODO: note to self, remember to convert to lowercase
from arachne.verbs import Verb
from arachne.nouns import Noun, Item
import re


# This tuple of tuples displays acceptable synonym regexes of each default action verb.
verb_lexicon = (
    (Verb.TAKE,      "^take$|^get$|^pick up$"),
    (Verb.DROP,      "^drop$"),
    (Verb.EXAMINE,   "^x |^check |^examine "),
    (Verb.PUT,       "^put$"),
    (Verb.INVENTORY, "^i$|^inventory$")
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
        a = str(split_input)
        b = "NO SUBJECT"
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


# TODO: Expand this
def _determine_subject(given_subject: str = None) -> tuple:
    results = []

    for obj in Noun.get_objects():
        # apply given pattern to all instances, add to a list (results) if matched
        search = re.search(given_subject, obj.name)
        if search: results.append(obj)

    print(results)

    if len(results) == 0:
        # in the case that no such string can be matched; subject doesn't exist
        return False, given_subject

    if len(results) > 1:
        # in the case that more than one item that matches given_subject, process all matches
        print("Which one?")
        for obj in enumerate(results, start = 1):
            # TODO: Pass results to a function to parse options.
            print(f"{obj[0]})", obj[1].name, end=" ")

    # finally return found object
    return True, results[0]



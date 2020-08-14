from arachne.verbs import Verb
import re


verb_lexicon = (
    (Verb.TAKE,      "^take$|^get$|^pick up$"),
    (Verb.DROP,      ""),
    (Verb.EXAMINE,   "^x |^check |^examine "),
    (Verb.PUT,       ""),
    (Verb.INVENTORY, "")
)


# Tokenizing function, parts out input into verb and subject fields.
def tokenize(given_str: str):
    a, b = _split_keywords(given_str)
    verb = _determine_verb(a)
    subject = _determine_subject(b)
    return verb, subject

# Following are private functions in the Pythonic sense.


# If input is a lone verb, no subject flag is raised
# and the appropriate event is executed.
def _split_keywords(given_str: str) -> tuple:
    split_input = given_str.split(' ', 1)

    if len(split_input) == 1:
        a = str(split_input)
        b = "NO SUBJECT"
        return a, b
    return tuple(split_input)


# Pattern regex for given verb, then return matching Verb enum for parsing.
def _determine_verb(given_verb: str) -> Verb:
    for entry in verb_lexicon:
        match = re.search(entry[1], given_verb)
        if match:
            return entry[0]
    return Verb.NULL


#TODO: Expand this
def _determine_subject(given_subject: str = None) -> str:
    return given_subject




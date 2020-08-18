import re

from arachne.lingo import Verb
from arachne.behaviors import Behavior as be
# here is where input is tokenized and sent to parser


# this tuple of tuples displays acceptable input that matches a universal verb using regex strings
verb_lexicon = (
    (Verb.LOOK, "^look$"),
    (Verb.TAKE, "^take$|^get$|^pick up$"),
    (Verb.DROP, "^drop$"),
    (Verb.EXAMINE, "^x$|^check$|^examine$"),
    (Verb.PUT, "^put$|^store$"),
    (Verb.INVENTORY, "^i$|^inventory$|^inv$")
)


# public tokenizing function, parts out input into verb and subject strings
def tokenize(given_str: str):
    a, b = _split_keywords(given_str)
    verb = _determine_verb(a)
    subject = _determine_subject(b)
    return verb, subject


# searches for a match using regexes in verb_lexicon, if no match return Verb.NULL constant
def _determine_verb(given_verb: str) -> Verb:
    for entry in verb_lexicon:
        found_match = re.search(entry[1], given_verb)
        if found_match:
            return entry[0]
    return Verb.NULL


def _determine_subject(given_subject: str) -> tuple:
    # in the case that a lone verb is inputted, prompt unspecified
    if given_subject == "":
        unspecified: tuple = (True, None)
        return unspecified

    subject: str = _trim_article(given_subject)
    results: list = list()

    vicinity = be.vicinity()
    for object_id in vicinity:
        instance = vicinity[object_id]
        if subject in instance.name:
            results.append(instance)

    # in the case that no such string can be matched; subject is nonexistent or not within reach
    if len(results) == 0:
        nonexistent: tuple = (False, subject)
        return nonexistent
    # in the case that more than one item that matches given_subject, process all matches
    if len(results) > 1:
        return _duplicates_resolution(results)

    # finally return found object
    found: tuple = (True, results[0])
    return found


# if input is a lone verb, return an empty subject string to raise lone verb flag.
def _split_keywords(given_str: str) -> tuple:
    split_input = given_str.split(' ', 1)

    # pack a tuple of (verb: str, subject: str) depending on input, then return
    if len(split_input) == 1:
        a: str = str(split_input[0])
        b: str = ""
        c: tuple = (a, b)
        return c
    return tuple(split_input)


# did you know? that articles are actually adjectives; they describe the nouns they precede.
def _trim_article(given_subject: str) -> str:
    articles: str = "a|an|the|some"
    matched = re.match(articles, given_subject)

    if matched:
        index: int = matched.end()
        return _trim_article(given_subject[index + 1:])
    return given_subject


def _duplicates_resolution(results: list) -> tuple:
    print("Which one?")

    for result in enumerate(results, start=1):
        print(f"{result[0]})", result[1].name, end=" ")

    choice: str = input("\n>")
    return _determine_subject(choice)

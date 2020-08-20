import re

from arachne.lingo import Verb, Subject, Prep
from arachne.behaviors import Behavior as be
# here is where input is tokenized and sent to parser


# this tuple of tuples displays acceptable input that matches a universal verb using regex strings
verb_lexicon = (
    (Verb.LOOK, "^look$|^look around$"),
    (Verb.TAKE, "^take$|^get$|^pick up$"),
    (Verb.DROP, "^drop$"),
    (Verb.EXAMINE, "^x$|^check$|^examine$"),
    (Verb.PUT, "^put$|^store$|^place$"),
    (Verb.INVENTORY, "^i$|^inventory$|^inv$"),
    (Verb.USE, "^use$|^consume$|^spend$")
)

preposition_lexicon = (
    (Prep.WITHIN, "in |inside |into "),
    (Prep.ATOP, "on |on top of |above "),
    (Prep.SETTING, "at |to ")
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


def _validate_subject(given_subject: str, results: list) -> Subject:
    if given_subject == "all": return Subject.ALL
    if given_subject == "": return Subject.UNSPECIFIED
    if len(results) == 0: return Subject.NONEXISTENT
    if len(results) > 1: return Subject.MULTIPLE
    return Subject.FOUND


# def _determine_preposition(given_subject: str) -> Prep:
#     for entry in preposition_lexicon:
#         found_match = re.search(entry[1], given_subject)
#         if found_match:
#             return entry[0]
#     return Verb


def _determine_subject(given_subject: str) -> tuple:
    subject: str = _trim_article(given_subject)
    results: list = list()

    # check vicinity for closest matching subject
    vicinity = be.vicinity()
    for object_id in vicinity:
        instance = vicinity[object_id]
        if subject in instance.name:
            results.append(instance)

    # check what kind of subject input this is
    validation = _validate_subject(subject, results)

    # if multiple matches, resolve the matches
    if validation is Subject.MULTIPLE: return _multiples_resolution(results)
    if validation is Subject.UNSPECIFIED: return validation, ""
    if validation is Subject.NONEXISTENT: return validation, subject

    subject_pair: tuple = (validation, results[0])
    return subject_pair


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
    articles: str = "^a |^an |^the |^some "
    matched = re.match(articles, given_subject)

    if matched:
        index: int = matched.end()
        return _trim_article(given_subject[index:])
    return given_subject


def _multiples_resolution(results: list) -> tuple:
    print("Which one?")

    for result in enumerate(results, start=1):
        print(f"{result[0]})", result[1].name, end=" ")

    choice: str = input("\n>")
    return _determine_subject(choice)

import re

from arachne.lingo import Verb, Object, Prep


# encompasses all known in-game vocabulary, unmatched vocab always default to type Object
lexicon = (
    ("ARTICLES", "^the$|^a$|^an$|^some$"),

    (Verb.LOOK, "^look$"),
    (Verb.TAKE, "^take$|^get$"),
    (Verb.DROP, "^drop$"),
    (Verb.PUT, "^put$|^store$|^place$"),
    (Verb.EXAMINE, "^x$|^check$|^examine$"),
    (Verb.INVENTORY, "^i$|^inv$|^inventory$"),
    (Verb.USE, "^use$|^consume$|^spend$"),

    (Verb.UNLOCK, "^unlock$"),
    (Verb.LOCK, "^lock$"),

    (Prep.WITHIN, "^in$|^inside$|^into$"),
    (Prep.ATOP, "^on$|^above$"),
    (Prep.SETTING, "^at$|^to$")
)


def tokenize(sentence: str, results: list) -> list:
    # snip first word from the sentence
    keywords: list = sentence.split(' ', 1)

    # input, even nonsensical input, defaults to subject if not otherwise defined
    key = Object.UNSPECIFIED
    word = keywords[0]

    # what kind of word is "word"? get the key if word found.
    for entry in lexicon:
        found = re.match(entry[1], word)
        if found:
            key = entry[0]

    # check if there was a subject in the last recursion.
    # we want to glue sequential subjects together.
    if len(results) >= 1:
        past_key = results[-1][0]
        if key == past_key:
            past_word = results[-1][1]
            results.pop()
            word = past_word + ' ' + word

    # if all else fails, word is a word of type "SUBJECT", so add it to our list as such
    results.append((key, word))

    # base case and recurse
    if len(keywords) == 1:
        return results
    return tokenize(keywords[1], results)

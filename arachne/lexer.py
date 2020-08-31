import re

from arachne.lingo import Object, lexicon


def tokenize(sentence: str, results: list) -> list:
    # snip first word from the sentence
    keywords: list = sentence.split(' ', 1)

    # input, even nonsensical input, defaults to an unspecified object if not found/defined
    key = Object.UNSPECIFIED
    word = keywords[0]

    # identify what kind of word we got from the split out of a list of words (verb, preposition, etc)
    for entry in lexicon:
        found = re.match(entry[1], word)
        if found:
            key = entry[0]

    # check if there was a object in the last recursion. glue sequential objects together.
    if len(results) >= 1:
        past_key = results[-1][0]
        if key == past_key:
            past_word = results[-1][1]
            results.pop()
            word = past_word + ' ' + word

    results.append((key, word))

    # base case and recurse
    if len(keywords) == 1:
        return results
    return tokenize(keywords[1], results)

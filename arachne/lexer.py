import string


class Filter:
    filter_tuple: tuple = (
        string.digits,
        string.punctuation
    )

    combined: str = ','.join(filter_tuple)

    @staticmethod
    def filter(given_str: str, combined: str = combined) -> list:
        filtered = Filter._filter(given_str, combined)
        return Lexer.tokenize(filtered)

    @staticmethod
    def _filter(given_str: str, combined: str) -> str:
        new_str: str = ''

        for char in given_str:
            if char in (i for i in combined):
                continue
            new_str += char

        return new_str


class Lexer:
    @staticmethod
    def tokenize(given_str: str) -> list:
        list_tokens: list = given_str.split()
        return list_tokens

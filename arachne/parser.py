from arachne.verbs import Verb


class Parser:
    @staticmethod
    def guess_verb(token: str) -> Verb:
        if token == "take":
            return Verb.TAKE

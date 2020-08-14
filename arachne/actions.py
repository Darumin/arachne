# TODO: PRIORITY -> This module might not even be necessary. Should be moved to parser.
# TODO: have actions DO something.
# TODO: Some actions must be able to receive tokens to customize default strings.

from arachne.verbs import Verb
from arachne.nouns import Item


def publish_action(action: Verb) -> None:
    if action is Verb.TAKE: Action.take()
    if action is Verb.EXAMINE: pass


class Action:
    @staticmethod
    def take(item: Item = None):
        if not item:
            return "There is nothing to take."
        return f"You take {item.name}"
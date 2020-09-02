from arachne.parser import write_action
from arachne.behaviors import setup_game

from dataclasses import dataclass
from arachne.nouns import Room


# just a form you fill out
@dataclass
class GameInfo:
    game_title: str
    byline: str
    preface: str
    start: Room


def start(game_info: GameInfo):

    game = setup_game(game_info)
    print(game.game_title)
    print(game.byline)
    print(game.preface)

    main_game_loop(game)


def main_game_loop(game):
    while True:
        command = input(">")
        if command == "quit": break
        if command == "$check":
            print(game.game_title)
            continue
        write_action(command)

from arachne.parser import write_action
from arachne.behaviors import setup_game
from arachne.nouns import GameInfo


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
        write_action(command)

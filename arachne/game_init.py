from arachne.parser import write_action


# temporary dummy init, for debugging purposes
class GameInit:
    @staticmethod
    def main_game_loop():
        while True:
            command = input(">")
            if command == "quit": break
            write_action(command)
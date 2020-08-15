from arachne.parser import write_action


# temporary dummy init, for debugging purposes
class GameInit:
    @staticmethod
    def main_game_loop():
        command = input(">")
        write_action(command)
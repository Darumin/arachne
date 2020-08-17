# This is an example script to help debug early iterations of Arachne.

from arachne.nouns import Room, Item
from arachne.behaviors import Behavior as be
from arachne.game import Game
from arachne.game_init import GameInit as start

blue_room = Room(
    name="The Blue Room",
    when_examined="A plain blue room.",
)

red_rose = Item(
    name="red rose",
    when_examined="By any other name, would smell as sweet.",
    when_encountered="Placed in a stone coffin."
)

blue_rose = Item(
    name="blue rose",
    when_examined="By any other name, it would smell as sweet.",
    when_encountered="Placed in a cement hearse."
)

be.add_to_container(blue_room, blue_rose)
be.add_to_container(blue_room, red_rose)
Game._start_location = blue_room
start.main_game_loop()

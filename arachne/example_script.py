# This is an example script to help debug early iterations of Arachne.

from arachne.game import Game
from arachne.nouns import Room, Item
from arachne.lingo import Desc
from arachne.game_init import GameInit

starting_room = Room("The Beginning")
red_rose = Item("the red rose")

red_rose.add_description(
    Desc.PLACEMENT, "A red rose has been planted in the"
    " stone planter here.")

starting_room.add_description(
    Desc.SELF, "A cool, low-ceilinged room"
    " with an LED light fixture casting a ghostly"
    " blue on the smooth, cemented floor. There is"
    " a smell of wax."
)

starting_room.add_item(red_rose)
Game.set_start(starting_room)

GameInit.main_game_loop()
# This is an example script to help debug early iterations of Arachne.

from arachne.nouns import Room, Item
from arachne.lingo import Desc

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

print(starting_room.describe_room())

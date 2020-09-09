import unittest

from arachne import behaviors as b
from arachne import nouns as n
from arachne import lingo as l
from arachne import game as g


# test game building functions
class PathingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.a = n.Room('A')
        self.b = n.Room('B')
        self.doo = n.Door('doo')

    def test_add_path_to(self):
        e = 'Should overwrite properly. Paths can be circular.'
        b.add_path_to(self.a, self.b, l.Compass.NORTH)
        b.add_path_to(self.a, self.a, l.Compass.NORTH)
        case_one = self.a.adjacency[l.Compass.NORTH] is self.a
        case_two = len(self.a.adjacency) == 1
        self.assertTrue(case_one and case_two, e)

    def test_add_door_to(self):
        e = 'Should add door to first room only, pointing to second room.'
        b.add_door_to(self.a, self.b, l.Compass.NORTH, self.doo)
        case_one = len(self.a.contents) == 1 and len(self.b.contents) == 0
        case_two = self.a.adjacency[l.Compass.NORTH] is self.b
        self.assertTrue(case_one and case_two, e)

    def test_bridge_paths(self):
        e = 'Rooms must reflect each other on compass.'
        b.bridge_paths(self.a, self.b, l.Compass.NORTH)
        case_one = self.a.adjacency[l.Compass.NORTH] == self.b
        case_two = self.b.adjacency[l.Compass.SOUTH] == self.a
        self.assertTrue(case_one and case_two, e)

    def test_bridge_doors(self):
        e = 'Rooms should `bridge_paths` using one door, maxing door.'
        b.bridge_doors(self.a, self.b, l.Compass.NORTH, self.doo)
        roo, comp = self.doo.room_context[id(self.b)]
        case = roo is self.a and comp is l.Compass.SOUTH and self.doo.is_maxed
        self.assertTrue(case, e)


# test functions for building game/interacting with game objects through interface
class ObjectStagingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.roo = n.Room('roo')
        self.box = n.Container('box')
        self.ite = n.Item('ite')
        self.key = n.Key('key')

        g.Player.current_location = self.roo

    def test_add_item_to(self):
        e = 'Should take multiple distinct item params.'
        b.add_item_to(self.roo, self.ite, self.ite, self.key)
        self.assertTrue(len(self.roo.contents) == 2, e)

    def remove_item_from(self):
        e = 'Should pop from contents dict.'
        b.add_item_to(self.box, self.key)
        b.remove_item_from(self.box, self.key)
        self.assertTrue(len(self.box.contents) == 0, e)

    def test_free_item(self):
        e = 'When adding items, should free `parent_container.`'
        b.add_item_to(self.box, self.ite)
        b.add_item_to(self.roo, self.ite)
        case = self.ite.parent_container
        self.assertTrue(case is self.roo, e)

    def test_vicinity(self):
        e = 'Everything in vicinity is active unless concealed.'
        b.add_item_to(self.box, self.ite)
        b.add_item_to(self.roo, self.key, self.box)
        self.assertTrue(len(b.vicinity()) == 3, e)

    def test_drop_on_floor(self):
        e = 'Should edit to dropped description and add to current location.'
        temp = self.ite.when_encountered
        b.drop_on_floor(self.ite)
        case_one = temp is not self.ite.when_encountered
        case_two = len(self.roo.contents) == 1
        self.assertNotEqual(case_one and case_two, e)

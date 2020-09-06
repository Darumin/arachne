import unittest
import arachne.game as g

from gc import get_objects


class GameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.one = g.Game('ar', 'ac', 'hn', 'e')
        self.two = g.Game('t', 'e', 's', 't')

    def test_id_equality(self):
        e = 'Both instances should be one and the same.'
        self.assertEqual(id(self.one), id(self.two), e)

    def test_singleton_instance(self):
        get = [o for o in get_objects() if o.__class__ is g.Game]
        e = 'Only one should exist.'
        self.assertTrue(len(get) == 1, e)

    def test_attr_assignment(self):
        self.one.game_title = 'baba'
        self.two.game_title = 'is you'
        e = 'Despite different instances, should overwrite first.'
        self.assertNotEqual(self.one.game_title, 'baba', e)
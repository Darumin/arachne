import unittest
import arachne.nouns as n
import arachne.utils as u


class NounTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.doo = n.Door('doo')
        self.con = n.Container('con')
        self.ite = n.Item('boo')

    def test_count_from_utils(self):
        cou = u.count_all_instances()
        a = cou['Door'] == 1 and cou['Container'] == 1 and cou['Item'] == 1
        self.assertTrue(a)

    def test_is_openable(self):
        e = 'Should classify properly.'
        self.assertTrue(self.doo.is_openable, e)
        self.assertFalse(self.ite.is_openable, e)

    def test_is_gettable(self):
        e = 'Should both default False.'
        a = self.doo.is_gettable and self.con.is_gettable
        self.assertFalse(a, e)

    def test_is_maxed(self):
        e = 'True if dict is outside capacity.'
        self.doo.room_context = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertTrue(self.doo.is_maxed, e)

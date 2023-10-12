#!/usr/bin/python3
""" Test file user """
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """ Test for City Class """

    def setUp(self):
        """ The setUp function """
        self.city = City()

    def tearDown(self):
        pass

    def test___init__(self):
        """ Test for __init__ function """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEquals(type(self.city.state_id), str)
        self.assertEquals(type(self.city.name), str)


if __name__ == "__main__":
    unittest.main()

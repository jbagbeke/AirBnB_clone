#!/usr/bin/python3
""" Test file amenity """
import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """ Test for Amenity Class """

    def setUp(self):
        """ The setUp function """
        self.amenity = Amenity()

    def tearDown(self):
        pass

    def test___init__(self):
        """ Test for __init__ function """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEquals(type(self.amenity.name), str)


if __name__ == "__main__":
    unittest.main()

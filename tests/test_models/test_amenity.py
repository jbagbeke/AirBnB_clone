#!/usr/bin/python3
""" Test file amenity """
import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """ Test for Amenity Class """

    def setUp(self):
        """ The setUp function """
        self.amenity = Amenity()

    def test_name_attribute(self):
        """This function tests the that the Amenity class 
        has the name attribute"""
        self.assertTrue(hasattr(self.amenity, "name"))
        message = "name should be of type str"
        self.assertIsInstance(self.amenity.name, str, message)
        self.assertEqual(self.amenity.name, "")

    def tearDown(self):
        del self.amenity


if __name__ == "__main__":
    unittest.main()

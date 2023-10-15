#!/usr/bin/python3
""" Test file user """
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """ Test for City Class """

    def setUp(self):
        """ The setUp function """
        self.city = City()

    def test_state_id_attribute(self):
        """This function tests the that the City 
        class has the state_id attribute"""
        self.assertTrue(hasattr(self.city, "state_id"))
        message = "state_id should be of type str"
        self.assertIsInstance(self.city.state_id, str, message)
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """This function tests the that the 
        City class has the name attribute"""
        self.assertTrue(hasattr(self.city, "name"))
        message = "name should be of type str"
        self.assertIsInstance(self.city.name, str, message)
        self.assertEqual(self.city.name, "")

    def tearDown(self):
        del self.city


if __name__ == "__main__":
    unittest.main()

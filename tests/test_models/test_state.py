#!/usr/bin/python3
""" Test file state """
import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """ Test for State Class """

    def setUp(self):
        """ The setUp function """
        self.state = State()

    def test_name_attribute(self):
        """This function tests the that the State 
        class has the name attribute"""
        self.assertTrue(hasattr(self.state, "name"))
        message = "name should be of type str"
        self.assertIsInstance(self.state.name, str, message)
        self.assertEqual(self.state.name, "")

    def tearDown(self):
        del self.state


if __name__ == "__main__":
    unittest.main()

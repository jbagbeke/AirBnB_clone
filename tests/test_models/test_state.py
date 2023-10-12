#!/usr/bin/python3
""" Test file state """
import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """ Test for State Class """

    def setUp(self):
        """ The setUp function """
        self.state = State()

    def tearDown(self):
        pass

    def test___init__(self):
        """ Test for __init__ function """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEquals(type(self.state.name), str)


if __name__ == "__main__":
    unittest.main()

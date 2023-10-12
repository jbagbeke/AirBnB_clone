#!/usr/bin/python3
""" Test file user """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        """ The setUp function """
        self.user = User()

    def tearDown(self):
        pass

    def test___init__(self):
        """ Test for __init__ function """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEquals(type(self.user.email), str)
        self.assertEquals(type(self.user.password), str)
        self.assertEquals(type(self.user.first_name), str)
        self.assertEquals(type(self.user.last_name), str)


if __name__ == "__main__":
    unittest.main()

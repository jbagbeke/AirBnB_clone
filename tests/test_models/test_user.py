#!/usr/bin/python3
""" Test file user """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        """ The setUp function """
        self.user = User()

    def test_email_attribute(self):
        """This function tests the that the User class has the email attribute"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """This function tests the that the User class has the password attribute"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """This function tests the that the User class has the first_name attribute"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """This function tests the that the User class has the last_name attribute"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")

    def tearDown(self):
        """ This is the Tear down function to destroy the user function"""
        del self.user


if __name__ == "__main__":
    unittest.main()

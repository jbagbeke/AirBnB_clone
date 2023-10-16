#!/usr/bin/python3
""" Test file review """
import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """ Test for Review Class """

    def setUp(self):
        """ The setUp function """
        self.review = Review()

    def test_place_id_attribute(self):
        """tests the that the Review class has the place_id attribute"""
        self.assertTrue(hasattr(self.review, "place_id"))
        type_str = "place_id should be of type str"
        self.assertIsInstance(self.review.place_id, str, type_str)
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """tests the that the Review class has the user_id attribute"""
        self.assertTrue(hasattr(self.review, "user_id"))
        type_str = "user_id should be of type str"
        self.assertIsInstance(self.review.user_id, str, type_str)
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """tests the that the Review class has the text attribute"""
        self.assertTrue(hasattr(self.review, "text"))
        type_str = "text should be of type str"
        self.assertIsInstance(self.review.text, str, type_str)
        self.assertEqual(self.review.text, "")

    def tearDown(self):
        """TearDown function to destroy the instance of review created"""
        del self.review


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" Test file for base_model """
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        """ The setUp function """
        self.model1 = BaseModel()

    def tearDown(self):
        self.model1.dispose()

    def test_save(self):
        """ Test for save function """
        self.assertEqual(type(self.model1.updated_at), datetime)

    def test_to_dict(self):
        """ The to_dict test """
        self.assertEqual(type(self.model1.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()

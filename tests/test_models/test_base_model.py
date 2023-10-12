#!/usr/bin/python3
""" Test file for base_model """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        """ The setUp function """
        self.model1 = BaseModel()

    def tearDown(self):
        pass

    def test_save(self):
        """ Test for save function """
        self.assertIsInstance(self.model1.updated_at, datetime)

    def test_to_dict(self):
        """ The to_dict test """
        self.assertEquals(type(self.model1.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()

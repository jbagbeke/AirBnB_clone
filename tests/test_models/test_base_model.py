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
        self.model2 = BaseModel()

    def test_id_attribute(self):
        """This function tests the that the model class has the id attribute"""
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertIsInstance(self.model1.id, str)

    def test_uuid(self):
        """This function tests the new instances created have unique ids"""
        self.assertFalse(self.assertEqual(self.model1.id, self.model2.id))

    def test_created_at_attribute(self):
        """This function tests the that the model class has the created_at attribute"""
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertIsInstance(self.model1.created_at, datetime)
        self.assertEqual(self.model1.created_at.isoformat(), self.model1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_updated_at_attribute(self):
        """This function tests the that the model class has the updated_at attribute"""
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertIsInstance(self.model1.updated_at, datetime)
        self.assertEqual(self.model1.updated_at.isoformat(), self.model1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_save(self):
        """ Test for save function """
        self.assertEqual(type(self.model1.updated_at), datetime)
        self.assertTrue(hasattr(self.model1, "save"))
        self.assertTrue(callable(self.model1.save))

    def test_to_dict(self):
        """ This function tests the to_dict function"""
        self.assertEqual(type(self.model1.to_dict()), dict)
        self.assertTrue(hasattr(self.model1, "to_dict"))
        self.assertTrue(callable(self.model1.to_dict))

    def test_str_(self):
        """ This is the test function to test the string representation of the BaseModel object"""
        self.assertTrue(hasattr(self.model1, "__str__"))
        self.assertTrue(callable(self.model1.__str__))

    def tearDown(self):
        """ This is the tear down function to destroy the model instance"""
        del self.model1
        del self.model2


if __name__ == "__main__":
    unittest.main()

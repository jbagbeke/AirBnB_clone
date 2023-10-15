#!/usr/bin/python3
""" Test file for base_model """
import unittest
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        """ The setUp function """
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.model3 = BaseModel()

    def test_id_attribute(self):
        """This function tests the that the model class has the id attribute"""
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertIsInstance(self.model1.id, str, "id should be of type str")

    def test_uuid(self):
        """Tests the new instances created have unique ids"""
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_created_at_attribute(self):
        """Tests the that the model class has the created_at attribute"""
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertIsInstance(self.model1.created_at, datetime.datetime, "created_at should be of type str")
        self.assertEqual(self.model1.created_at.isoformat(), self.model1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_updated_at_attribute(self):
        """Tests the that the model class has the updated_at attribute"""
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertIsInstance(self.model1.updated_at, datetime.datetime, "updated_at should be of type str")
        self.assertEqual(self.model1.updated_at.isoformat(), self.model1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_save(self):
        """ Test for save function """
        self.assertTrue(hasattr(self.model1, "save"))
        self.assertTrue(callable(self.model1.save))
        assert self.model1 in storage.all().values()

    def test_to_dict(self):
        """ This function tests the to_dict function"""
        self.assertEqual(type(self.model1.to_dict()), dict)
        self.assertTrue(hasattr(self.model1, "to_dict"))
        self.assertTrue(callable(self.model1.to_dict))

    def test_str_(self):
        """ Test the string representation of the BaseModel object"""
        self.assertTrue(hasattr(self.model1, "__str__"))
        self.assertTrue(callable(self.model1.__str__))

    def tearDown(self):
        """ Tear down function to destroy the model instance"""
        del self.model1
        del self.model2


if __name__ == "__main__":
    unittest.main()

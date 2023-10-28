#!/usr/bin/python3
""" Test file for base_model """
import unittest
import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import json
import os


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
        str_type = "created_at should be of type str"
        creat_ed_at = self.model1.created_at
        self.assertIsInstance(creat_ed_at, datetime.datetime, str_type)
        strf_time = self.model1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.model1.created_at.isoformat(), strf_time)

    def test_updated_at_attribute(self):
        """Tests the that the model class has the updated_at attribute"""
        self.assertTrue(hasattr(self.model1, "updated_at"))
        update_str = "updated_at should be of type str"
        updat_ed_at = self.model1.updated_at
        self.assertIsInstance(updat_ed_at, datetime.datetime, update_str)
        strf_time = self.model1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.model1.updated_at.isoformat(), strf_time)

    def test_save(self):
        """ Test for save function """
        self.assertTrue(hasattr(self.model1, "save"))
        self.assertTrue(callable(self.model1.save))
        assert self.model1 in storage.all().values()
        with self.assertRaises(TypeError) as e:
            self.model1.save(50)
        message2 = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), message2)

    def test_to_dict(self):
        """ This function tests the to_dict function"""
        self.assertEqual(type(self.model1.to_dict()), dict)
        self.assertTrue(hasattr(self.model1, "to_dict"))
        self.assertTrue(callable(self.model1.to_dict))
        with self.assertRaises(TypeError) as e:
            self.model1.to_dict(self, 45)
        message = "to_dict() takes 1 positional argument but 3 were given"
        self.assertEqual(str(e.exception), message)
        self.model1.name = "Laura"
        self.model1.age = 23
        self.model2 = self.model1.to_dict()
        self.assertEqual(self.model2["id"], self.model1.id)
        self.assertEqual(self.model2["__class__"], type(self.model1).__name__)
        self.assertEqual(self.model2["created_at"], self.model1.created_at.isoformat())
        self.assertEqual(self.model2["updated_at"], self.model1.updated_at.isoformat())
        self.assertEqual(self.model2["name"], self.model1.name)
        self.assertEqual(self.model2["age"], self.model1.age)

    def test_str_(self):
        """ Test the string representation of the BaseModel object"""
        self.assertTrue(hasattr(self.model1, "__str__"))
        self.assertTrue(callable(self.model1.__str__))
        u = self.model1.id
        dict_ = self.model1.__dict__
        ex_rep = "[BaseModel] ({}) {}".format(u, dict_)
        actual_rep = self.model1.__str__()
        self.assertEqual(ex_rep, actual_rep)

    def tearDown(self):
        """ Tear down function to destroy the model instance"""
        del self.model1
        del self.model2


if __name__ == "__main__":
    unittest.main()

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
        self.model1.resetStorage()
        with self.assertRaises(TypeError) as e:
            self.model1.save()
        message = "save() missing 1 required positional argument: self"
        self.assertEqual(str(e.exception), message)
        self.model1.resetStorage()
        with self.assertRaises(TypeError) as e:
            self.model1.save(self, 50)
        message2 = "save() contains excess positional arguments"
        self.model1.resetStorage()
        self.assertEqual(str(e.exception), message2)
        self.model1.resetStorage()
        self.model1.save()
        key = "{}.{}".format(type(self.model1).__name__, self.model1.id)
        self.model2 = {key: self.model1.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(self.model2)))
            f.seek(0)
            self.assertEqual(json.load(f), self.model2)

    def test_to_dict(self):
        """ This function tests the to_dict function"""
        self.assertEqual(type(self.model1.to_dict()), dict)
        self.assertTrue(hasattr(self.model1, "to_dict"))
        self.assertTrue(callable(self.model1.to_dict))
        self.model1.resetStorage()
        with self.assertRaises(TypeError) as e:
            self.model1.to_dict(self, 45)
        message = "to_dict() contains excess positional arguments"
        self.assertEqual(str(e.exception), message)
        self.model1.resetStorage()
        with self.assertRaises(TypeError) as e:
            self.model1.to_dict()
        message2 = "to_dict() requires 1 positional argument: self"
        self.assertEqual(str(e.exception), message2)
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

    def tearDown(self):
        """ Tear down function to destroy the model instance"""
        del self.model1
        del self.model2


if __name__ == "__main__":
    unittest.main()

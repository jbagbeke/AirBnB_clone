#!/usr/bin/python3
""" The test module for file_Storage """
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ This is the test class for FileStorage """

    def setUp(self):
        """ The setUp function """
        self.files = FileStorage()

    def test_file_path_attribute(self):
        """This function tests the that the FileStorage class has the __file_path attribute"""
        self.assertFalse(hasattr(self.files, "__file_path"))

    def test_objects_attribute(self):
        """This function tests the that the FileStorage class has the __objects attribute"""
        self.assertFalse(hasattr(self.files, "__objects"))

    def test_all(self):
        """This function tests the that the FileStorage class has the all function"""
        self.assertTrue(hasattr(self.files, "all"))
        self.assertTrue(callable(self.files.all))

    def test_new(self):
        """This function tests the that the FileStorage class has the new function"""
        self.assertTrue(hasattr(self.files, "new"))
        self.assertTrue(callable(self.files.new))

    def test_save(self):
        """This function tests the that the FileStorage class has the save function"""
        self.assertTrue(hasattr(self.files, "save"))
        self.assertTrue(callable(self.files.save))

    def test_reload(self):
        """This function tests the that the FileStorage class has the reload function"""
        self.assertTrue(hasattr(self.files, "reload"))
        self.assertTrue(callable(self.files.reload))

    def tearDown(self):
        """ The tearDown function """
        del self.files


if __name__ == "__main__":
    unittest.main()

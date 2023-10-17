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
        """Tests that the FileStorage class has the __file_path attribute"""
        self.assertFalse(hasattr(self.files, "__file_path"))
        self.assertIsInstance(self.files.__file_path, str, "__file_path should be of type str")

    def test_objects_attribute(self):
        """Tests that the FileStorage class has the __objects attribute"""
        self.assertFalse(hasattr(self.files, "__objects"))
        self.assertIsInstance(self.files.__objects, dict, "__objects should be of type dict")

    def test_all(self):
        """Tests that the FileStorage class has the all function"""
        self.assertTrue(hasattr(self.files, "all"))
        self.assertTrue(callable(self.files.all))
        self.assertEqual(self.files.all(), self.files.__objects)

    def test_new(self):
        """Tests that the FileStorage class has the new function"""
        self.assertTrue(hasattr(self.files, "new"))
        self.assertTrue(callable(self.files.new))
        with self.assertRaises(TypeError) as e:
            self.files.new(self, 45)
        message = "new() takes 2 positional argument but 3 were given"
        self.assertEqual(str(e.exception), message)

    def test_save(self):
        """Tests that the FileStorage class has the save function"""
        self.assertTrue(hasattr(self.files, "save"))
        self.assertTrue(callable(self.files.save))
        with self.assertRaises(TypeError) as e:
            self.files.save(50)
        message = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), message)

    def test_reload(self):
        """Tests that the FileStorage class has the reload function"""
        self.assertTrue(hasattr(self.files, "reload"))
        self.assertTrue(callable(self.files.reload))

    def tearDown(self):
        """ The tearDown function """
        del self.files


if __name__ == "__main__":
    unittest.main()

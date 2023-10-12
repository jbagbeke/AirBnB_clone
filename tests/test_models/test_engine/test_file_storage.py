#!/usr/bin/python3
""" The test module for file_Storage """
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ This is the test class for FileStorage """

    def setUp(self):
        """ The setUp function """
        self.files = FileStorage()

    def tearDown(self):
        """ The tearDown function """
        pass

    def test___init__(self):
        """ This is the test for the object initialization function """
        self.assertTrue(hasattr(self.files, "__file_path"))
        self.assertTrue(hasattr(self.files, "__objects"))
        self.assertEquals(type(self.files.__filepath), str)
        self.assertEquals(type(self.files.__objects), dict)

    def test_all(self):
        """ The test for the all function """
        self.assertEquals(type(self.files.all()), dict)


if __name__ == "__main__":
    unittest.main()

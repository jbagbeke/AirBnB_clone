#!/usr/bin/python3
""" Test file place """
import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """ Test for Place Class """

    def setUp(self):
        """ The setUp function """
        self.place = Place()

    def tearDown(self):
        pass

    def test___init__(self):
        """ Test for __init__ function """
        self.assertTrue(hasattr(self.place, "place"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEquals(type(self.place.place), str)
        self.assertEquals(type(self.place.user_id), str)
        self.assertEquals(type(self.place.name), str)
        self.assertEquals(type(self.place.description), str)
        self.assertEquals(type(self.place.number_rooms), int)
        self.assertEquals(type(self.place.number_bathrooms), int)
        self.assertEquals(type(self.place.max_guest), int)
        self.assertEquals(type(self.place.price_by_night), int)
        self.assertEquals(type(self.place.latitude), float)
        self.assertEquals(type(self.place.longitude), float)
        self.assertEquals(type(self.place.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()

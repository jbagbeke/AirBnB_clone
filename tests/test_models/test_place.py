#!/usr/bin/python3
""" Test file place """
import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """ Test for Place Class """

    def setUp(self):
        """ The setUp function """
        self.place = Place()

    def test_city_id_attribute(self):
        """This function tests the that the Place class has the city_id attribute"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """This function tests the that the Place class has the user_id attribute"""
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """This function tests the that the Place class has the name attribute"""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """This function tests the that the Place class has the description attribute"""
        self.assertTrue(hasattr(self.place, "description"))
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        """This function tests the that the Place class has the number_rooms attribute"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """This function tests the that the Place class has the number_bathrooms attribute"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """This function tests the that the Place class has the max_guest attribute"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        """This function tests the that the Place class has the price_by_night attribute"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        """This function tests the that the Place class has the latitude attribute"""
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)
    
    def test_longitude_attribute(self):
        """This function tests the that the Place class has the longitude attribute"""
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        """This function tests the that the Place class has the amenity_ids attribute"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def tearDown(self):
        del self.place


if __name__ == "__main__":
    unittest.main()

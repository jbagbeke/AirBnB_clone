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
        """Tests the that the Place class has the city_id attribute"""
        self.assertTrue(hasattr(self.place, "city_id"))
        type_str = "city_id should be of type str"
        self.assertIsInstance(self.place.city_id, str, type_str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """Tests the that the Place class has the user_id attribute"""
        self.assertTrue(hasattr(self.place, "user_id"))
        type_str = "user_id should be of type str"
        self.assertIsInstance(self.place.user_id, str, type_str)
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """Tests the that the Place class has the name attribute"""
        self.assertTrue(hasattr(self.place, "name"))
        type_str = "name should be of type str"
        self.assertIsInstance(self.place.name, str, type_str)
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """Tests the that the Place class has the description attribute"""
        self.assertTrue(hasattr(self.place, "description"))
        type_str = "description should be of type str"
        self.assertIsInstance(self.place.description, str, type_str)
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        """Tests the that the Place class has the number_rooms attribute"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        type_str = "number_rooms should be of type int"
        self.assertIsInstance(self.place.number_rooms, int, type_str)
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """Tests the that the Place class has the number_bathrooms attribute"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        type_str = "number_bathrooms should be of type int"
        self.assertIsInstance(self.place.number_bathrooms, int, type_str)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """Tests the that the Place class has the max_guest attribute"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        type_str = "max_guest should be of type int"
        self.assertIsInstance(self.place.max_guest, int, type_str)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        """Tests the that the Place class has the price_by_night attribute"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        type_str = "price_by_night should be of type int"
        self.assertIsInstance(self.place.price_by_night, int, type_str)
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        """Tests the that the Place class has the latitude attribute"""
        self.assertTrue(hasattr(self.place, "latitude"))
        type_str = "latitude should be of type float"
        self.assertIsInstance(self.place.latitude, float, type_str)
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attribute(self):
        """Tests the that the Place class has the longitude attribute"""
        self.assertTrue(hasattr(self.place, "longitude"))
        type_str = "longitude should be of type float"
        self.assertIsInstance(self.place.longitude, float, type_str)
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        """Tests the that the Place class has the amenity_ids attribute"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        type_str = "amenity_ids should be of type list"
        self.assertIsInstance(self.place.amenity_ids, list, type_str)
        self.assertEqual(self.place.amenity_ids, [])

    def tearDown(self):
        """The tear down function"""
        del self.place


if __name__ == "__main__":
    unittest.main()

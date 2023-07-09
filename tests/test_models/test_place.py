#!/usr/bin/python3

"""Module for testing Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class for testing the Place"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_place = Place()

    def test_place_exists(self):
        """Test the existance and type of Place object"""
        self.assertTrue(self.my_place)
        self.assertEqual(type(self.my_place), Place)

    def test_city_id_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.city_id, "")

    def test_user_id_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.user_id, "")

    def test_name_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.name, "")

    def test_description_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.description, "")

    def test_number_room_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.number_rooms, 0)

    def test_number_bathrooms_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.number_bathrooms, 0)

    def test_max_guest_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.max_guest, 0)

    def test_price_by_night_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.price_by_night, 0)

    def test_latitude_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.latitude, 0.0)

    def test_longitude_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.longitude, 0.0)

    def test_amenity_ids_exist(self):
        """Test the attributes of place exist"""
        self.assertEqual(self.my_place.amenity_ids, [])

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

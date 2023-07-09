#!/usr/bin/python3

"""Module for testing City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class for testing the City"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_city = City()

    def test_city_exists(self):
        """Test the existance and type of city object"""
        self.assertTrue(self.my_city)
        self.assertEqual(type(self.my_city), City)

    def test_city_state_id_exist(self):
        """Test the attributes of city existance"""
        self.assertEqual(self.my_city.state_id, "")

    def test_city_name_exist(self):
        """Test the attributes of city existance"""
        self.assertEqual(self.my_city.name, "")

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

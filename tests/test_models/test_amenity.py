#!/usr/bin/python3

"""Module for testing Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class for testing the Amenity"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_amen = Amenity()

    def test_amen_exists(self):
        """Test the existance and type of amen object"""
        self.assertTrue(self.my_amen)
        self.assertEqual(type(self.my_amen), Amenity)

    def test_amen_name_exist(self):
        """Test the attributes of amen existance"""
        self.assertEqual(self.my_amen.name, "")

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

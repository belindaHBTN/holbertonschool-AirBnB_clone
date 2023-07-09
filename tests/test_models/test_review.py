#!/usr/bin/python3

"""Module for testing Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class for testing the Review"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_rev = Review()

    def test_rev_exists(self):
        """Test the existance and type of Review object"""
        self.assertTrue(self.my_rev)
        self.assertEqual(type(self.my_rev), Review)

    def test_rev_place_id_exist(self):
        """Test the attributes of Review existance"""
        self.assertEqual(self.my_rev.place_id, "")

    def test_rev_user_id_exist(self):
        """Test the attributes of Review existance"""
        self.assertEqual(self.my_rev.user_id, "")

    def test_rev_text_exist(self):
        """Test the attributes of Review existance"""
        self.assertEqual(self.my_rev.text, "")

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

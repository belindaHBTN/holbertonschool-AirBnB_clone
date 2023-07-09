#!/usr/bin/python3

"""Module for testing User class"""
import unittest
from models.user import User
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Class for testing the User"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_user = User()

    def test_user_exists(self):
        """Test the existance and type of user object"""
        self.assertTrue(self.my_user)
        self.assertEqual(type(self.my_user), User)

    def test_user_first_name_exist(self):
        """Test the attributes of user existance"""
        self.assertEqual(self.my_user.first_name, "")

    def test_user_last_name_exist(self):
        """Test the attributes of user existance"""
        self.assertEqual(self.my_user.last_name, "")

    def test_user_email_exist(self):
        """Test the attributes of user existance"""
        self.assertEqual(self.my_user.email, "")

    def test_user_password_exist(self):
        """Test the attributes of user existance"""
        self.assertEqual(self.my_user.password, "")

    def test_user_attributes_type(self):
        """Test the attributes of user type"""
        self.assertEqual(type(self.my_user.id), str)
        self.assertEqual(type(self.my_user.created_at), datetime)
        self.assertEqual(type(self.my_user.updated_at), datetime)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.last_name), str)
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

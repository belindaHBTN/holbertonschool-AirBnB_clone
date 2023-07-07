#!/usr/bin/python3

"""Module for testing BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing the BaseModel"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_save(self):
        """Test is the save method is functioning correctly"""
        update_time = self.my_model.updated_at
        self.my_model.save()
        new_update_time = self.my_model.updated_at
        self.assertNotEqual(update_time, new_update_time)

    def test_id(self):
        """Tests the random id alloction"""
        self.assertTrue(self.my_model.id)
        self.my_model_2 = BaseModel()
        self.assertNotEqual(self.my_model.id, self.my_model_2.id)

    def test_str(self):
        """Test the string return value"""
        formatted_string = self.my_model.__str__
        self.assertTrue(formatted_string)
        instance_for_test = BaseModel()
        self.assertEqual(str(instance_for_test), instance_for_test.__str__())

    def test_to_dict_type(self):
        """Test the to_dict method is functioning correctly"""
        test_dict = self.my_model.to_dict()
        self.assertEqual(type(test_dict), dict)

    def test_to_dict(self):
        """Test the to_dict method is functioning correctly"""
        test_dict = self.my_model.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue(test_dict["__class__"])
        self.assertTrue(test_dict["id"])
        self.assertTrue(test_dict["my_number"])
        self.assertTrue(test_dict["updated_at"])
        self.assertTrue(test_dict["created_at"])

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

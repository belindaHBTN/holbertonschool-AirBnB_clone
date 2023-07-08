#!/usr/bin/python3

"""Module for testing FileStorage class"""
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    """Class for testing the FileStorage"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.fs = FileStorage()
        kwargs = {
            "name": "My test base model",
            "id": "42",
            "my_number": 3.14,
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now())
        }
        self.bm1 = BaseModel(**kwargs)

    def test_file_path(self):
        """Test the file path class attribute"""
        test_path = self.fs._FileStorage__file_path
        self.assertEqual(test_path, "file.json")

    def test_objects_dict(self):
        """Test the class attribute objects"""
        test_obj_dict = self.fs._FileStorage__objects
        self.assertEqual(type(test_obj_dict), dict)

    def test_all_method(self):
        """Test the instance method all"""
        test_obj_dict = self.fs._FileStorage__objects
        test_all_dict = self.fs.all()
        self.assertDictEqual(test_obj_dict, test_all_dict)

    def test_new_method(self):
        """Test the instance method new"""
        self.bm1.save()
        test_obj_dict_1 = self.fs._FileStorage__objects
        self.assertEqual(test_obj_dict_1["BaseModel.42"], self.bm1)
        storage.new(self.bm1)
        self.assertTrue(test_obj_dict_1["BaseModel.42"])

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        try:
            os.remove(self.fs._FileStorage__file_path)
        except FileNotFoundError:
            pass

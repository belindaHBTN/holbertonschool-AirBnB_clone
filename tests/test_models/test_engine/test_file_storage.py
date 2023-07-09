#!/usr/bin/python3

"""Module for testing FileStorage class"""
import unittest
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class for testing the FileStorage"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.fs = FileStorage()
        kwargs = {
            "name": "My test base model 1",
            "id": "11",
            "my_number": 1111,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        self.bm = BaseModel(**kwargs)

        self.test_path = self.fs._FileStorage__file_path
        self.fs.new(self.bm)
        self.fs.save()
        self.fs.reload()
        self.obj_dict = self.fs.all()

    def test_file_path(self):
        """Test the file path class attribute"""
        self.assertEqual(self.test_path, "file.json")

    def test_objects_dict(self):
        """Test the class attribute objects"""
        self.assertEqual(type(self.obj_dict), dict)

    def test_new_method(self):
        """Test the instance method new"""
        self.assertIn("BaseModel.11", self.obj_dict)

    def test_save_method(self):
        """Test the instance method save"""
        self.assertTrue(os.path.exists(self.test_path))
        with open(self.test_path, "r", encoding='utf-8') as a_file:
            data = json.load(a_file)
        self.assertIn("BaseModel.11", data)

    def test_reload_method(self):
        """Test the instance method reload"""
        new_fs = FileStorage()
        new_fs.reload()
        new_obj_dict = new_fs.all()
        self.assertEqual(self.obj_dict, new_obj_dict)

    def test_reload_method_obj(self):
        obj_old = self.obj_dict["BaseModel.11"]
        obj_new = BaseModel(**obj_old.to_dict())
        self.assertEqual(obj_old.to_dict(), obj_new.to_dict())

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        try:
            os.remove(self.fs._FileStorage__file_path)
        except FileNotFoundError:
            pass

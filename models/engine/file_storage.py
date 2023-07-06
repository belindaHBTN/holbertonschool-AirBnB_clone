#!/usr/bin/python3

"""This model serializes instances to a JSON file and deserializes
JSON file to instances"""
import json
import os


class FileStorage:
    """FileStorage Class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initialise attrs"""
        pass

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """add a key-value pair for each instance into the objects dict"""
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        key = obj_class_name + "." + obj_id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objects dictionary to the JSON file"""
        with open(FileStorage.__file_path, "w") as a_file:
            json.dump(FileStorage.__objects, a_file)

    def reload(self):
        """deserializes the JSON file to objects dictionary"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as b_file:
                FileStorage.__objects = json.load(b_file)

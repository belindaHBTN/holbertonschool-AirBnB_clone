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
        self.__objects[key] = obj

    def save(self):
        """serializes objects dictionary to the JSON file"""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        try:
            with open(FileStorage.__file_path, "w") as a_file:
                json.dump(new_dict, a_file)
        except:
            pass

    def reload(self):
        """deserializes the JSON file to objects dictionary"""
        from models.base_model import BaseModel
        from models.user import Us
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_name_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        dict_objects = {}
        try:
            with open(self.__file_path, "r") as b_file:
                dict_objects = json.load(b_file)
        except:
            dict_objects = {}
            pass
        for key, value in dict_objects.items():
            class_name_str = value["__class__"]
            if class_name_str in class_name_dict:
                class_name = class_name_dict[class_name_str]
                FileStorage.__objects[key] = class_name(**value)
            else:
                raise TypeError(f"unknown class: {current_class}")

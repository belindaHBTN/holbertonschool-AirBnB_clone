#!/usr/bin/python3

"""This model defines all attributes/methods for other classes"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base Class that define all common attrs and methods"""

    def __init__(self, *args, **kwargs):
        """initialise attrs"""
        attributes_ignore_list = ["__class__"]
        attribute_datetime_list = ['created_at', 'updated_at']
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attributes_ignore_list:
                    continue
                elif key in attribute_datetime_list:
                    setattr(self, key, datetime.now().fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return a string to represent the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """generate a dictionary representation of an instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.isoformat(self.created_at)
        my_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return my_dict

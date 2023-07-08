#!/usr/bin/python3

"""This module defines all attributes/methods for User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines all attributes/methods"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3

"""This module defines all attributes/methods for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines all attributes/methods"""
    place_id = ""
    user_id = ""
    text = ""

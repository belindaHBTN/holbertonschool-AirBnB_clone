#!/usr/bin/python3

"""This model "create a unique FileStorage instance for application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

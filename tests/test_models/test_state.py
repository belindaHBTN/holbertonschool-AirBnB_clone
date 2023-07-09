#!/usr/bin/python3

"""Module for testing State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class for testing the State"""

    def setUp(self):
        """Create an instance for use in testing"""
        self.my_state = State()

    def test_state_exists(self):
        """Test the existance and type of state object"""
        self.assertTrue(self.my_state)
        self.assertEqual(type(self.my_state), State)

    def test_name_exist(self):
        """Test the attributes of state existance"""
        self.assertEqual(self.my_state.name, "")

    def tearDown(self):
        """Clean up the instance that was used for testing"""
        pass

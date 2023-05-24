#!/usr/bin/python3
"""This is the test for state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """This is the class for test state"""

    def test_initialization(self):
        state = State()
        self.assertEqual(
            str(type(state)), "<class 'models.state.State'>")
        self.assertEqual(state.name, "")

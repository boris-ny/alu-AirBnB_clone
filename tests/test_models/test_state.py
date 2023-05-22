#!/usr/bin/python3
"""Test for State class"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State
import unittest
import os

class Test_State(TestBaseModel):
    """State class testing"""
    
    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
    
    def test_name(self):
        """testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

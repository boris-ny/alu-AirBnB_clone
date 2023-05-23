#!/usr/bin/python3
"""Test for Amenity class"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity

class Test_Amenity(TestBaseModel):
    """Testing Amenity class"""

    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
    
    def test_name(self):
        """testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
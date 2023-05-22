#!/usr/bin/python3
"""Test for Place class"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place
import os

class Test_Place(TestBaseModel):
    """Testing place class"""

    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
    
    def test_city_id(self):
        """testing city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv("HBNB_TYPE_STORAGE") != "db" else type(None))
        
    def test_user_id(self):
        """testing user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv("HBNB_TYPE_STORAGE") != "db" else type(None))
        
    def test_name(self):
        """testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """testing description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """testing number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)
    
    def test_number_bathrooms(self):
        """testing number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)
    
    def test_max_guest(self):
        """testing max guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """testing price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """testing latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)
    
    def test_longitude(self):
        """testing longitude"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """testing amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

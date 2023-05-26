#!/usr/bin/python
"""Testing Place module"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Place class testing"""
    def setUp(self):
        """Place class testing setup"""
        self.place = Place()

    def test_attributes(self):
        """Testing Place attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_str(self):
        place = Place()
        self.assertEqual(place.__class__, Place)

    def test_parent(self):
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))


if __name__ == "__main__":
    unittest.main()

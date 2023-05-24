#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class"""
    def setUp(self):
        """Amenity class testing setup"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Testing Amenity attributes"""
        self.assertEqual(
            str(type(self.amenity)), "<class 'models.amenity.Amenity'>")
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()

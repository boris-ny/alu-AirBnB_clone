#!/usr/bin/python3
"""This the test for the city class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_attr(self):
        """City testing setup"""
        self.city = City()
        self.assertEqual(
            str(type(City)), "<class 'models.city.City'>")
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")


if __name__ == "__main__":
    unittest.main()

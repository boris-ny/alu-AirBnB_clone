#!/usr/bin/python3
import unittest
from models.place import Place


class TestBase(unittest.TestCase):
    def test_initialization(self):
        place = Place()
        self.assertEqual(
            str(type(place)), "<class 'models.place.Place'>")
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, {})


if __name__ == "__main__":
    unittest.main()

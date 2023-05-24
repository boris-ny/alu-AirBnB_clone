#!/usr/bin/python3
"""This is the test for review"""
import unittest
from models.review import Review

def test_initialization(self):
        review = Review()
        self.assertEqual(
            str(type(review)), "<class 'models.review.Review'>")
        self.assertEqual(review.text, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")



if __name__ == "__main__":
    unittest.main()

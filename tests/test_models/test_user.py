#!/usr/bin/python3
"""Testing User module"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """User class testing"""
    def setUp(self):
        """User class testing setup"""
        self.user = User()

    def test_attributes(self):
        """Testing User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_str(self):
        user = User()
        self.assertEqual(user.__class__, User)

    def test_parent(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

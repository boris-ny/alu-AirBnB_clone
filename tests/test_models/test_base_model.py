#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import json
import os

class TestBaseModel(unittest.TestCase):
    """This class tests the BaseModel class"""
    def setUp(self):
        """This method sets up the tests"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        self.base3 = BaseModel()

    def tearDown(self):
        """This method tears down the tests"""
        del self.base1
        del self.base2
        del self.base3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """This method tests the attributes of BaseModel"""
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertFalse(hasattr(self.base1, "random_attr"))
        self.assertEqual(self.base1.__class__.__name__, "BaseModel")
        self.assertEqual(self.base1.id, self.base1.id)
        self.assertEqual(self.base1.created_at, self.base1.created_at)
        self.assertEqual(self.base1.updated_at, self.base1.updated_at)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        self.assertNotEqual(self.base1.updated_at, self.base2.updated_at)
        self.assertEqual(self.base1.__class__.__name__, self.base2.__class__.__name__)

    def test_created_at(self):
        """This method tests the created_at attribute"""
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertEqual(self.base1.created_at, self.base1.created_at)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        self.assertEqual(type(self.base1.created_at), datetime)

    def test_updated_at(self):
        """This method tests the updated_at attribute"""
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertEqual(self.base1.updated_at, self.base1.updated_at)
        self.assertNotEqual(self.base1.updated_at, self.base2.updated_at)
        self.assertEqual(type(self.base1.updated_at), datetime)

    def test_save(self):
        """This method tests the save method"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)
        self.assertEqual(type(self.base1.updated_at), datetime)

    def test_to_dict(self):
        """This method tests the to_dict method"""
        self.base1
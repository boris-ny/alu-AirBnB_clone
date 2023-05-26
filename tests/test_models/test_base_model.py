#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Testing BaseModel class"""

    def test_init(self):
        model = BaseModel()
        self.assertEqual(
            str(type(model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(str(type(model.id)), "<class 'str'>")
        self.assertEqual(
            str(type(model.created_at)), "<class 'datetime.datetime'>")
        self.assertEqual(
            str(type(model.updated_at)), "<class 'datetime.datetime'>")

    def test_str(self):
        """test str method"""
        model = BaseModel()
        self.assertEqual(
            str(model), "[{}] ({}) {}".format(
                model.__class__.__name__, model.id, model.__dict__))

    def test_save(self):
        """test save method"""
        model = BaseModel()
        model.save()
        self.assertEqual(model.created_at, model.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(str(type(model_dict["created_at"])), "<class 'str'>")
        self.assertEqual(str(type(model_dict["updated_at"])), "<class 'str'>")
        self.assertEqual(str(type(model_dict["id"])), "<class 'str'>")


if __name__ == "__main__":
    unittest.main()

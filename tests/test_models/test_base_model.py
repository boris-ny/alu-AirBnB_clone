#!/usr/bin/python3
"""Testing for BaseModel class"""
import unittest
import datetime
from models.base_model import BaseModel
import os
from uuid import UUID
import json
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """Testing class for BaseModel"""

    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Setting up"""
        self.name = "BaseModel"
        self.value = BaseModel

    def tearDown(self):
        """Cleaning up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pycode(self):
        """Testing for pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_default(self):
        """Testing for default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Testing for kwargs"""
        i = self.value(id="56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(type(i.id), str)
        self.assertEqual(i.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")

    def test_save(self):
        """Testing for save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            dic = json.load(f)
            self.assertEqual(dic[key], i.to_dict())

    def test_str(self):
        """Testing for str"""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, i.id,
                                                       i.__dict__))

    def test_to_dict(self):
        """Testing for to_dict"""
        i = self.value()
        i_dict = i.to_dict()
        self.assertEqual(type(i_dict), dict)
        self.assertTrue(hasattr(i_dict, "__class__"))
        self.assertEqual(type(i_dict["created_at"]), str)
        self.assertEqual(type(i_dict["updated_at"]), str)
        self.assertEqual(i_dict["__class__"], self.name)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
    Defines unittests for 'models/engine/file_storage.py'
    Unittest classes:
        TestFileStorage_instantiation
        TestFileStorage_methods
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment"""
        cls.storage = FileStorage()

    def setUp(self):
        """Set up before each test method"""
        TestFileStorage.storage.reload()

    def tearDown(self):
        """Clean up after each test method"""
        TestFileStorage.storage.reload()

    def test_all_method_returns_dict(self):
        """Test if the 'all' method returns a dictionary"""
        result = TestFileStorage.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_object(self):
        """Test if the 'new' method adds the object to __objects"""
        obj = BaseModel()
        TestFileStorage.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, TestFileStorage.storage.all())

    def test_save_method_saves_to_file(self):
        """Test if the 'save' method saves objects to the file"""
        obj = BaseModel()
        TestFileStorage.storage.new(obj)
        TestFileStorage.storage.save()
        with open(TestFileStorage.storage._FileStorage__file_path) as f:
            data = f.read()
        self.assertIn(obj.id, data)

    def test_reload_method_loads_objects(self):
        """Test if the 'reload' method loads objects from the file"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        TestFileStorage.storage.new(obj)
        TestFileStorage.storage.save()
        TestFileStorage.storage.reload()
        self.assertIn(key, TestFileStorage.storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_reload_method_handles_file_not_found(self, mock_stdout):
        """Test if the 'reload' method handles FileNotFound error"""
        TestFileStorage.storage._FileStorage__file_path = "non_existent_file.json"
        TestFileStorage.storage.reload()
        self.assertEqual(mock_stdout.getvalue().strip(), "")


if __name__ == '__main__':
    unittest.main()

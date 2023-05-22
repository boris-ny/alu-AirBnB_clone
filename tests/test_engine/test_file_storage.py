import unittest
import os
import json
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_adds_to_objects(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_writes_to_file(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(obj.id, data)

    def test_reload_loads_from_file(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        # Clear objects
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = obj.__class__.__name__ + "." + obj.id
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_reload_ignores_missing_file(self):
        # Ensure reload does not raise an exception if the file is missing
        self.storage.reload()

    def test_delete_removes_object(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.delete(obj)
        self.assertNotIn(obj, self.storage._FileStorage__objects)

    def test_close_calls_reload(self):
        with patch('models.file_storage.FileStorage.reload') as mock_reload:
            self.storage.close()
            mock_reload.assert_called_once()

if __name__ == '__main__':
    unittest.main()

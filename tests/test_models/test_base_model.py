import unittest
from datetime import datetime
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dictionary(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        base_model_dict = self.base_model.to_dict()
        self.assertCountEqual(base_model_dict.keys(), expected_keys)

    def test_to_dict_created_at_format(self):
        base_model_dict = self.base_model.to_dict()
        created_at_str = base_model_dict['created_at']
        self.assertEqual(created_at_str, self.base_model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        base_model_dict = self.base_model.to_dict()
        updated_at_str = base_model_dict['updated_at']
        self.assertEqual(updated_at_str, self.base_model.updated_at.isoformat())

    def test_delete_calls_storage_delete(self):
        with unittest.mock.patch('models.storage.delete') as mock_delete:
            self.base_model.delete()
            mock_delete.assert_called_once_with(self.base_model)

if __name__ == '__main__':
    unittest.main()

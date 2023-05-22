import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init_no_args(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:30:00.000000',
            'name': 'test',
            'value': 42
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2022, 1, 1, 12, 30, 0))
        self.assertEqual(obj.name, 'test')
        self.assertEqual(obj.value, 42)

    def test_str(self):
        obj = BaseModel()
        obj_str = str(obj)
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj_str, expected_str)

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, prev_updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_with_additional_attributes(self):
        obj = BaseModel()
        obj.name = 'test'
        obj.value = 42
        obj_dict = obj.to_dict()
        self.assertIn('name', obj_dict)
        self.assertEqual(obj_dict['name'], 'test')
        self.assertIn('value', obj_dict)
        self.assertEqual(obj_dict['value'], 42)

if __name__ == '__main__':
    unittest.main()

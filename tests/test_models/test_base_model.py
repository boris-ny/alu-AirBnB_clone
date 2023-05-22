import unittest
from models import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test that the class can be initialized with no arguments"""
        model = BaseModel()
        self.assertEqual(model.id, str(uuid.uuid4()))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        # Test that the class can be initialized with keyword arguments
        model = BaseModel(id="1234567890", created_at="2023-05-22T15:45:00.000Z", updated_at="2023-05-22T15:45:00.000Z")
        self.assertEqual(model.id, "1234567890")
        self.assertEqual(model.created_at, datetime.fromisoformat("2023-05-22T15:45:00.000Z"))
        self.assertEqual(model.updated_at, datetime.fromisoformat("2023-05-22T15:45:00.000Z"))

    def test_str(self):
        """Test that the string representation of the class is correct"""
        model = BaseModel()
        expected_string = "[BaseModel] (1234567890) {'id': '1234567890', 'created_at': '2023-05-22T15:45:00.000Z', 'updated_at': '2023-05-22T15:45:00.000Z'}"
        self.assertEqual(str(model), expected_string)

    def test_save(self):
        # Test that the save method updates the updated_at attribute
        model = BaseModel()
        before_save = model.updated_at
        model.save()
        after_save = model.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict(self):
        # Test that the to_dict method returns a dictionary containing all keys/values of __dict__ of the instance
        model = BaseModel()
        expected_dict = {
            "id": model.id,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
        }
        self.assertEqual(model.to_dict(), expected_dict)

    def test_delete(self):
        # Test that the delete method deletes the current instance from the storage
        model = BaseModel()
        models.storage.add(model)
        self.assertTrue(model in models.storage)
        model.delete()
        self.assertFalse(model in models.storage)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage
import json

class FileStorage:
    """
    class FileStorage
    Represent the file storage engine
    It serializes instances to a JSON file and deserializes JSON file to instances
    """


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method
        Returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        Public instance method
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Public instance method
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w") as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as f:
                serialized = json.load(f)
                for key in serialized.values():
                    self.new(eval(key["__class__"] + "(**" + str(key) + ")"))
        except FileNotFoundError:
            pass

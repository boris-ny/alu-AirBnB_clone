#!/usr/bin/python3
"""This module defines a class for File Storage"""
import json


class FileStorage:
    """This class serializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
<<<<<<< HEAD
        return Filestorage.__objects
=======
        return FileStorage.__objects
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.to_dict()
                           ['id']: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(Filestorage.__file_path, 'w') as f:
            temp = {}
            temp.update(Filestorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        try:
            temp = {}
            with open(Filestorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    Filestorage.__objects[key] = \
                        classes[val['__class__']](**val)
        except FileNotFoundError:
<<<<<<< HEAD
            print('File not found')
=======
            print("File not found")
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

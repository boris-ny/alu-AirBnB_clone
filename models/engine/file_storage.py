#!/usr/bin/python3
"""This module is for the FileStorage class"""
import json
import os
import datetime

class FileStorage():
    """
    Class for storing and retrieving data
    
    Attributes:
        __file_path: path to the JSON file
        __objects: dictionary to store objects
    
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w',encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r',encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                new_dict[key] = eval(value["__class__"])(**value)
            FileStorage.__objects = new_dict
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is None:
            key = obj.__class__.__name__ + "." + obj.id
            del FileStorage.__objects[key]

    def close(self):
        """Calls reload() method"""
        self.reload()
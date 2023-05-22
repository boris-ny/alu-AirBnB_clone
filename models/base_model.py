#!/usr/bin/python3
"""This module is for the BaseModel class for all other classes"""

import uuid
from datetime import datetime
import models

class BaseModel():
    """This class is the base model for all other classes"""
    def __init__(self, *args, **kwargs):
        """This method initializes the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method returns the string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
    
    def delete(self):
        """This method deletes the current instance from the storage"""
        models.storage.delete(self)
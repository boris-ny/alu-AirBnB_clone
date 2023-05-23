#!/usr/bin/python3
"""This module defines a class BaseModel"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """A base class for all models"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
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
            models.storage.save()

    def __str__(self):
        """Return a string representation of this BaseModel instance."""
        cls = (str(type(self)).split(".")[-1]).split("\'")[0]
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of this BaseModel instance."""
        dictionary= {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':(str(type(self)).split(".")[-1]).split("\'")[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
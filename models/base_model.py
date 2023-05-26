#!/usr/bin/python3
"""Base model class"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """Initialization method"""

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                elif key != "__class__":
                    self.__dict__[key] = value
                else:
                    models.storage.new(self)

    def __str__(self):
        """Returns string representation of instance"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Save the current instance to the storage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of the model instance"""
        returndict = self.__dict__.copy()
        returndict["__class__"] = self.__class__.__name__
        returndict["created_at"] = self.created_at.isoformat()
        returndict["updated_at"] = self.updated_at.isoformat()
        return returndict

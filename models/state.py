#!/usr/bin/python3
"""This module defines a class State"""
from models.base_model import BaseModel,Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models

class State(BaseModel,Base):
    """
    Represents a State for a MySQL database.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals to the
            current State.id as private attribute from __objects
            """
            cities_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    def __init__(self, *args, **kwargs):
        """
        Initializes a State.
        """
        super().__init__(*args, **kwargs)

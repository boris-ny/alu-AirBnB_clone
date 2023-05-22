#!/usr/bin/python3
"""This module defines a class Amenity"""
from models.base_model import BaseModel,Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

class Amenity(BaseModel,Base):
    """
    Represents an Amenity for a MySQL database.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity.
        """
        super().__init__(*args, **kwargs)
#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """AMENITY CLASS"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)

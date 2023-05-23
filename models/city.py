#!/usr/bin/python3
"""This module creates a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a City object"""
        super().__init__(*args, **kwargs)

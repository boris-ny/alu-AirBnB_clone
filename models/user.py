#!/usr/bin/python3
"""The module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a User object"""
        super().__init__(*args, **kwargs)

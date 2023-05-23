#!/usr/bin/python3
<<<<<<< HEAD
"""The module creates a User class"""
=======
"""Module for User class"""
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """Instantiates a User object"""
        super().__init__(*args, **kwargs)
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb

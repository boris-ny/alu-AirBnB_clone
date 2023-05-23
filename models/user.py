#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""The module creates a User class"""
=======
"""Module for User class"""
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
=======
"""Module for User class"""
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

    def __init__(self, *args, **kwargs):
        """Instantiates a User object"""
        super().__init__(*args, **kwargs)
<<<<<<< HEAD
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
=======
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

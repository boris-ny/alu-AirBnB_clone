#!/usr/bin/python3
"""This is State module for AirBnB"""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State"""
        super().__init__(*args, **kwargs)


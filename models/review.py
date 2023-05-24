#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: The place id
        user_id: The user id
        text: input text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

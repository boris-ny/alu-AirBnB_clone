<<<<<<< HEAD
#!/usr/bin/python3
"""This module creates a Review class"""

=======
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """Instantiates a Review object"""
        super().__init__(*args, **kwargs)
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb

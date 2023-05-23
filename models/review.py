<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/python3
"""This module creates a Review class"""

=======
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
=======
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

    def __init__(self, *args, **kwargs):
        """Instantiates a Review object"""
        super().__init__(*args, **kwargs)
<<<<<<< HEAD
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
=======
>>>>>>> 9d13ffd5ceb620a4ee8d857f99814e12541b88d5

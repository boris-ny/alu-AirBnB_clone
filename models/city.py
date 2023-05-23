<<<<<<< HEAD
#!/usr/bin/python3
"""This module creates a city class"""

=======
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb
from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """Instantiates a City object"""
        super().__init__(*args, **kwargs)
>>>>>>> 3d797718ce7e50dc59d13958c124892886e6ecbb

#!/usr/bin/python3	
"""This module defines a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                            Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     primary_key=True,
                                     nullable=False),
                            Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True,
                                     nullable=False))
class Place(BaseModel,Base):
    """
    Represents a Place for a MySQL database.
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                viewonly=False
                                backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a Place.
        """
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """
        Returns the list of Review instances with
        place_id equals to the current Place.id
        """
        review_list = []
        for review in models.storage.all('Review').values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            amenity_list = []
            for amenity in models.storage.all('Amenity').values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
#!/usr/bin/python3
"""
    Place class inherits BaseModel
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
        Class place
    """

    name = ""
    description = ""
    user_id = ""
    city_id = ""
    number_romms = 0
    number_bathrooms = 0
    max_guests = 0
    price_bynight = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


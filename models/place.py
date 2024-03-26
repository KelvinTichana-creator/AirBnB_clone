#!/usr/bin/python3
"""The `place` module

This module defines the Place class, which represents a place/house in the application.

Attributes:
    name (str): The name of the place/house.
    user_id (str): The ID of the user who uploaded the place/house.
    city_id (str): The ID of the city where the place/house is located.
    description (str): Description of the place/house.
    number_bathrooms (int): Number of bathrooms in the place/house.
    price_by_night (int): Price per night for the place/house.
    number_rooms (int): Number of rooms in the place/house.
    longitude (float): Longitude coordinate of the place/house location.
    latitude (float): Latitude coordinate of the place/house location.
    max_guest (int): Maximum number of guests allowed in the place/house.
    amenity_ids (list): List of amenity IDs associated with the place/house.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place/house in the application.

    Attributes:
        name (str): The name of the place/house.
        user_id (str): The ID of the user who uploaded the place/house.
        city_id (str): The ID of the city where the place/house is located.
        description (str): Description of the place/house.
        number_bathrooms (int): Number of bathrooms in the place/house.
        price_by_night (int): Price per night for the place/house.
        number_rooms (int): Number of rooms in the place/house.
        longitude (float): Longitude coordinate of the place/house location.
        latitude (float): Latitude coordinate of the place/house location.
        max_guest (int): Maximum number of guests allowed in the place/house.
        amenity_ids (list): List of amenity IDs associated with the place/house.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Place object."""
        super().__init__(*args, **kwargs)
        self.name = ""
        self.user_id = ""
        self.city_id = ""
        self.description = ""
        self.number_bathrooms = 0
        self.price_by_night = 0
        self.number_rooms = 0
        self.longitude = 0.0
        self.latitude = 0.0
        self.max_guest = 0
        self.amenity_ids = []


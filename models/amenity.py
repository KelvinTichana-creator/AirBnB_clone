#!/usr/bin/python3
"""The `amenity` module

This module defines the Amenity class, which represents an amenity provided by a place/house.

Attributes:
    name (str): The name of the amenity.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity provided by a place/house.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity object."""
        super().__init__(*args, **kwargs)
        self.name = ""


#!/usr/bin/python3
"""The `review` module.

This module defines the Review class, which represents a review of a place/house.

Attributes:
    text (str): The text content of the review.
    user_id (str): The ID of the user who posted the review.
    place_id (str): The ID of the place/house being reviewed.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review of a place/house.

    Attributes:
        text (str): The text content of the review.
        user_id (str): The ID of the user who posted the review.
        place_id (str): The ID of the place/house being reviewed.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Review object."""
        super().__init__(*args, **kwargs)
        self.text = ""
        self.user_id = ""
        self.place_id = ""


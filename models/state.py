#!/usr/bin/python3
"""The `state` module

This module defines the State class, which represents a state in the application.

Attributes:
    name (str): The name of the state.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state in the application.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new State object."""
        super().__init__(*args, **kwargs)
        self.name = ""


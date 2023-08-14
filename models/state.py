#!/usr/bin/python3
"""used to define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Used to represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

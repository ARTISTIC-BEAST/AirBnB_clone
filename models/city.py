#!/usr/bin/python3
"""creating the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Attributes for this city class:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

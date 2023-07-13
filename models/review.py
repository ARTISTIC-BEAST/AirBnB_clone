#!/usr/bin/python3
"""creates the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Attributes for this review class:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

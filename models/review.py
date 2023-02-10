#!/usr/bin/python3
"""Defines the Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review

    Args:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): The text of the review
    """
    
    place_id = ""
    user_id = ""
    text = ""

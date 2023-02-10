#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Review class."""
=======
"""Defines the Review Class."""
>>>>>>> a20f467b2b216445c0ff216b86884efa10529ae2
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

=======
    """Represent a review

    Args:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): The text of the review
    """
    
>>>>>>> a20f467b2b216445c0ff216b86884efa10529ae2
    place_id = ""
    user_id = ""
    text = ""

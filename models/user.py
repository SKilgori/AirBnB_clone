#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Args:
        email (str): The email of the user.
        password (str): The pasword of the user.
        first_name (str): The frst name of the user.
        last_name (str): The last name of the user.
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

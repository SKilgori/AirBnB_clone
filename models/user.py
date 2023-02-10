#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

=======
    """Represents a User.

    Args:
        email (str): The email of the user.
        password (str): The pasword of the user.
        first_name (str): The frst name of the user.
        last_name (str): The last name of the user.
    """
    
>>>>>>> a20f467b2b216445c0ff216b86884efa10529ae2
    email = ""
    password = ""
    first_name = ""
    last_name = ""

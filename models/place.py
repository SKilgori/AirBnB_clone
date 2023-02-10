#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Place class."""
=======
"""Defines the Place class. """
>>>>>>> a20f467b2b216445c0ff216b86884efa10529ae2
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
<<<<<<< HEAD
    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
=======
    Args:
        city_id (str): The city id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The numver of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number if guests of the place.
        price_by_night (int): The price per night.
        latitute (float): The latitude
        logitude (float): The longitude.
        amenity_ids (list): A list of Amenity ids.
    """
    
    city_id = ""
    user_id = ""
    name = ""
    descrption = ""
>>>>>>> a20f467b2b216445c0ff216b86884efa10529ae2
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

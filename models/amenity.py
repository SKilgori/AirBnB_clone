#!/usr/bin/python3
"""Defines the Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Args:
        name (string): The name of the amenity.
    """
    
    name = ""

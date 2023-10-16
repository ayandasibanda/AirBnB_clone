#!/usr/bin/python3
'''Amenity class, inheriting from BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Representation of an amenity in the application'''

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of Amenity."""
        super().__init__(*args, **kwargs)

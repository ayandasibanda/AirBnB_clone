#!/usr/bin/python3
'''Module defining the City class, inheriting from BaseModel'''

from models.base_model import BaseModel


class City(BaseModel):
    '''City class for the application'''

    state_id = ""  # State ID associated with the city
    name = ""      # Name of the city

    def __init__(self, *args, **kwargs):
        """Initializes a City instance"""

        super().__init__(*args, **kwargs)
        # Call the constructor of the parent class (BaseModel)
        # to initialize common attributes such as id, created_at, and updated_at


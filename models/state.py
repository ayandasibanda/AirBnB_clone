#!/usr/bin/python3
'''Module defining the State class, inheriting from BaseModel'''

from models.base_model import BaseModel


class State(BaseModel):
    '''State class for the application'''

    name = ""   # Name of the state

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""

        super().__init__(*args, **kwargs)
        # Call the constructor of the parent class (BaseModel)
        # to initialize common attributes such as id, created_at, and updated_at


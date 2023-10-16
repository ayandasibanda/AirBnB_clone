#!/usr/bin/python3
'''Module defining the Review class, inheriting from BaseModel'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class for the application'''

    place_id = ""   # Place ID associated with the review
    user_id = ""    # User ID associated with the review
    text = ""       # Text content of the review

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance"""

        super().__init__(*args, **kwargs)
        # Call the constructor of the parent class (BaseModel)
        # to initialize common attributes such as id, created_at, and updated_at


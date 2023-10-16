#!/usr/bin/python3
'''Module defining the User class, inheriting from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User class representing a user in the application'''

    email = ""        # Email address of the user
    password = ""     # Password associated with the user's account
    first_name = ""    # First name of the user
    last_name = ""     # Last name of the user

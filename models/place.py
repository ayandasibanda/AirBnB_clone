#!/usr/bin/python3
'''Module defining the Place class, inheriting from BaseModel'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''Place class for the application'''

    city_id = ""            # City ID associated with the place
    user_id = ""            # User ID associated with the place
    name = ""               # Name of the place
    description = ""        # Description of the place
    number_rooms = 0        # Number of rooms in the place
    number_bathrooms = 0    # Number of bathrooms in the place
    max_guest = 0           # Maximum number of guests the place can accommodate
    price_by_night = 0      # Price per night for the place
    latitude = 0.0          # Latitude coordinate of the place
    longitude = 0.0         # Longitude coordinate of the place
    amenity_ids = []        # List of amenity IDs associated with the place

    def __init__(self, *args, **kwargs):
        """Initializes a Place instance"""

        super().__init__(*args, **kwargs)
        # Call the constructor of the parent class (BaseModel)
        # to initialize common attributes such as id, created_at, and updated_at


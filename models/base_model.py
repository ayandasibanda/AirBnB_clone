#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        # Define the datetime format used for string parsing
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

        # Generate a unique identifier for the instance
        self.id = str(uuid4())

        # Set the creation and update times to the current datetime
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # If keyword arguments are provided, populate instance attributes
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                # Convert datetime strings to datetime objects
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, datetime_format)
                else:
                    # Set other attributes directly
                    self.__dict__[key] = value
        else:
            # If no kwargs provided, add the instance to storage
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        # Update the updated_at attribute
        self.updated_at = datetime.today()

        # Save the object to storage
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        # Create a copy of the instance dictionary
        result_dict = self.__dict__.copy()

        # Convert datetime objects to ISO formatted strings
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()

        # Add the class name to the dictionary
        result_dict["__class__"] = self.__class__.__name__

        return result_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        # Get the class name for the string representation
        class_name = self.__class__.__name__

        # Return a formatted string representation
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


#!/usr/bin/python3
'''Module defining the BaseModel class'''

import uuid
from datetime import datetime
import models


class BaseModel():
    '''BaseModel class for the application'''

    def __init__(self, *args, **kwargs):
        '''Constructor for the BaseModel class'''

        if kwargs:
            # Convert string representation of datetime to datetime object
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            # Set attributes from kwargs
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            # Initialize with new id, created_at, and updated_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add the new instance to storage
            models.storage.new(self)

    def __str__(self):
        '''String representation of BaseModel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''Update 'updated_at' instance with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Dictionary representation of instance'''
        new_dict = dict(self.__dict__)
        # Convert datetime objects to ISO format strings
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict


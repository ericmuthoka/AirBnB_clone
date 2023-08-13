#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
from models.engine import storage  # Import the storage variable


class BaseModel:
    """BaseModel class that defines common attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Call new(self) method on storage for new instances
            storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute with the current datetime
        and call save() method of storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary with keys/values of instance attributes."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

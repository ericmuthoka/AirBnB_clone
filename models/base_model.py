#!/usr/bin/python3

import uuid
import datetime


class BaseModel:
    """Base class for other models."""

    id = None
    created_at = None
    updated_at = None

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary with all
        keys/values of __dict__ of the instance."""
        dict_ = {k: v for k, v in self.__dict__.items() if v is not None}
    dict_['__class__'] = self.__class__.__name__
    dict_['created_at'] = self.created_at.isoformat()
    dict_['updated_at'] = self.updated_at.isoformat()
    return dict_

#!/usr/bin/python3
"""File Storage"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """FileStorage class for serializing and
    deserializing instances to/from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    value['created_at'] = datetime.strptime(value['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    value['updated_at'] = datetime.strptime(value['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    cls = eval(class_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

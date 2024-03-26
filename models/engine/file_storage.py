#!/usr/bin/python3
"""
Module: file_storage.py

This module defines the FileStorage class for serializing and deserializing instances to/from a JSON file.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """
    Manages the serialization and deserialization of instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to __objects.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists.
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    deserialized = json.load(f)
                except json.JSONDecodeError:
                    deserialized = None

                if deserialized:
                    FileStorage.__objects = {
                        k: current_classes[k.split('.')[0]](**v)
                        for k, v in deserialized.items()}


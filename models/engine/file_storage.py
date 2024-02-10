#!/usr/bin/python3
"""
    This model contains all file storage class
    and als serializes inst to JSON file and deserisalizes
    JSON file instances
"""
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import json

class FileStorage:
    """
        Represents file storage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the dict objects
        """
        return self.__objects

    def new(self,obj):
        """
            sets in objects the new obj
        """
        if obj:
            keys = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[keys] = obj

    def save(self):
        """
            serializez objects to the JSON
        """
        file_name = self.__file_path
        data = {}
        for keys, value in self.__objects.items():
            data[keys] = value.to dict()
            with open(file_name, "w") as file:
                json.dump(data, file)

    def reload(self):
        """
            Deserialisation JSON file to objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for value in object_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""
    This module defines the Base_Model class
"""

import uuid
import datetime
import models

class Basemodel:
    """
        Defines all common attributes for other class
    """

    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
         else:
            kwargs["created_at"] = datetime.datetime.strptime(
                kwargs["created_at"],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["updated_at"] = datetime.datetime.strptime(
                kwargs["updated_at"],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            for keys, value in kwargs.items():
                if keys != "__class__":
                    setattr(self, keys, value)


    def save(self):
        """
            Updates the self updatee with the current date time
        """
        self.updated_at = datetime.utcnow()
        #CALL THE SAVE
        models.storage.save()

        def __str__(self):
        """
            Returns everything in base model as string
        """
        string = "[{}] ({}) {}"
        return string.format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
            Turning an instance to Passing self to Dictionary
        """
        dcti = self.__dict__.copy()
        #access and manipulate project atributes
        dcti["__class__"] = self.__class__.__name__
        dcti["created_at"] = self.created_at.isoformat()
        dcti["updated_at"] = self.updated_at.isoformat()

        return dcti

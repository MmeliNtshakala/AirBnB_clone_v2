#!/usr/bin/python3
"""
    This module defines the Base_Model class
"""

import uuid
from datetime import datetime


class Basemodel:
    """
        Defines all common attributes for other class
    """

    def __init__(self):
        seld.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
            Updates the self updatee with the current date time
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
            Turning an instance to Passing self to Dictionary
        """
        inst_dict = self.__dict__.copy()
        #access and manipulate project atributes
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict


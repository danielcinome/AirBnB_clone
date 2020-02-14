#!/usr/bin/python3
"""
    Base Models
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self):
        """
            Contructor
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()


    def __str__(self):
        """
            Str function
        """
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)


    def save(self):
        """
            Save function
        """
        self.updated_at = datetime.today()

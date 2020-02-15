#!/usr/bin/python3
"""
    Base Models
"""
from uuid import uuid4
from datetime import datetime
from models import storage
import json


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
            Contructor
        """
        if len(kwargs) >= 1:
            dateCreate = kwargs['created_at']
            dateUpdate = kwargs['updated_at']
            formato = '%Y-%m-%dT%H:%M:%S.%f'
            dateCreate = datetime.strptime(dateCreate, formato)
            dateUpdate = datetime.strptime(dateUpdate, formato)
            kwargs['created_at'] = dateCreate
            kwargs['updated_at'] = dateUpdate
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """
            Str function
        """
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        """
            Save function
        """
        if type(self.updated_at) is str:
            self.updated_at = str(datetime.today())
        else:
            self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
            To Dictionary function
        """
        rDict = self.__dict__
        rDict['created_at'] = str(self.created_at.isoformat())
        rDict['updated_at'] = str(self.updated_at.isoformat())
        dicName = {"__class__": self.__class__.__name__}
        rDict.update(dicName)
        return rDict

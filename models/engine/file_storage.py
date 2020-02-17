#!/usr/bin/python3
"""
    FileStorage class that serializes instances in
    a JSON file and deserializes the JSON file
"""
import json
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage():

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Return the dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, 'w') as my_json:
            copy = {}
            for key, value in self.__objects.items():
                copy[key] = value.to_dict()
            dic_ser = json.dumps(copy)
            my_json.write(dic_ser)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as my_json:
                red = json.loads(my_json.read())
                for key, value in red.items():
                    splKey = key.split(".")
                    copy = globals()[splKey[0]](**value)
                    self.__objects[key] = copy
        except IOError:
            return

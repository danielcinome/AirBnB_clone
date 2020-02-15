#!/usr/bin/python3
"""
    FileStorage class that serializes instances in
    a JSON file and deserializes the JSON file
"""
import json
from .. import base_model



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
        dic = obj.__str__
        val_id  = obj.id
        name = obj.__class__.__name__
        FileStorage.__objects[name + '.' + val_id] = obj
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj = FileStorage.__objects
        dic = {}
        for key, value in obj.items():
            dic[key] = value.__dict__
            dic[key]['created_at'] = dic[key]['created_at'].isoformat()
            dic[key]['updated_at'] = dic[key]['updated_at'].isoformat()
        dic_ser = json.dumps(dic)
        with open(FileStorage.__file_path, 'w') as my_json:
            my_json.write(dic_ser)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as my_json:
                red = json.loads(my_json.read())
                for key, value in red.items():
                    print(issubclass(self, type(BaseModel)))
                    new = self(value)
                    FileStorage.__objects[key] = new
        except IOError:
            return

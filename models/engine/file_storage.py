#!/usr/bin/python3
"""
Class that saves instances to a JSON file
and reads JSON file to instances
"""
import json
import os


class FileStorage:
    """
    Class that reads and saves JSON objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves objects to JSON file
        """
        dic = {}

        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        """
        Read objects from the JSON file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        from models.city import City

        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))

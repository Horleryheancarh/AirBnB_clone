#!/usr/bin/python3
"""
Parent Model Class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines common attributes and method
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Return string repof class name, id and attribute dictionary
        """
        class_name = '[' + self.__class__.__name__ + ']'
        dic = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + ' (' + self.id + ') ' + str(dic)

    def save(self):
        """
        Update updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Creates a new dictionary
        """
        dic = {}

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dic[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                if not value:
                    pass
                else:
                    dic[key] = value

        dic['__class__'] = self.__class__.__name__

        return dic

#!/usr/bin/python3
"""
BaseModel Unittests
"""
import unittest
import os
import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class BaseModelTests(unittest.TestCase):
    """
    BaseModel Tests
    """
    my_model = BaseModel()

    def testBaseModel1(self):
        """
        Test attributes of BaseModel
        """

        self.my_model.name = 'John Doe'
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """
        Test Update
        """
        self.my_model.first_name = 'Jane'
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        dict1 = self.my_model.to_dict()

        self.my_model.first_name = 'Johnny'
        self.my_model.save()

        dict2 = self.my_model.to_dict()

        self.assertEqual(dict1['created_at'], dict2['created_at'])
        self.assertNotEqual(dict2['updated_at'], dict2['updated_at'])


if __name__ == '__main__':
    unittest.main()

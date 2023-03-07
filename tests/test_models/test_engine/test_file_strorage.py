#!/usr/bin/python3
"""
Unittests Module
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTesets(unittest.TestCase):
    """
    File Storage Tests
    """

    my_model = BaseModel()

    def testClasssInstance(self):
        """
        Check Instance
        """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """
        Test Save and Reload Methods
        """
        self.my_model.full_name = "Jane Doe"
        self.my_model.save()
        my_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = my_dict['__class__'] + '.' + my_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """
        Test Save, Update and Reload Methods
        """
        self.my_model.full_name = "Jane Doe"
        self.my_model.save()
        my_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = my_dict['__class__'] + '.' + my_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(my_dict['my_name'], 'Jane Doe')

        create1 = my_dict['created_at']
        update1 = my_dict['updated_at']

        self.my_model.full_name = "John Dame"
        self.my_model.save()
        my_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = my_dict['created_at']
        update2 = my_dict['updates_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(my_dict['my_name'], 'John Dame')

    def testHasAttributes(self):
        """
        Verify Attributes
        """
        self.assertEqual(hasattr(FileStorage, '__FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '__FileStorage__file_path'), True)

    def testSave(self):
        """
        Verify JSON exists
        """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testReload(self):
        """
        Test Reload
        """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        
        obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)

        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(obj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """
        Check save self
        """
        msg = "save() takes i positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def testSaveFileStorage(self):
        """
        Test if new method is working
        """
        in1 = self.my_model.to_dict()
        new_key = in1['__class__'] + '.' + in1['id']
        storage.save()

        with open('file.json', 'r') as f:
            in2 = json.load(f)

        new = in2[new_key]
        for key in key2:
            self.assertEqual(in1[key], new[key])

if __name__ == '__main__':
    unittest.main()

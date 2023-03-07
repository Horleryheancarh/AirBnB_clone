#!/usr/bin/python3
"""
Unitest for amenity
"""
import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Tests instance and methods from amenity model
    """
    a = Amenity()

    def test_class_exists(self):
        """
        class exists
        """
        clss = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), clss)

    def test_user_inheritance(self):
        """
        test if its a subclass of BaseModel
        """
        self.assertIsInstance(self.a, Amenity)

    def testHasAttributes(self):
        """
        Verify if attributes exist
        """
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self):
        """
        Verify if attributes types
        """
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

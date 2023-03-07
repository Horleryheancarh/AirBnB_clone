#!/usr/bin/python3
"""
Unitest for amenity
"""
import unittest
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    Tests instance and methods from city model
    """
    a = City()

    def test_class_exists(self):
        """
        class exists
        """
        clss = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.a)), clss)

    def test_user_inheritance(self):
        """
        test if its a subclass of BaseModel
        """
        self.assertIsInstance(self.a, City)

    def testHasAttributes(self):
        """
        Verify if attributes exist
        """
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'state_id'))

    def test_types(self):
        """
        Verify if attributes types
        """
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)
        self.assertIsInstance(self.a.state_id, str)


if __name__ == '__main__':
    unittest.main()

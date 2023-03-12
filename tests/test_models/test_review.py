#!/usr/bin/python3
"""
Unitest for amenity
"""
import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Tests instance and methods from amenity model
    """
    a = Review()

    def test_class_exists(self):
        """
        class exists
        """
        clss = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.a)), clss)

    def test_user_inheritance(self):
        """
        test if its a subclass of BaseModel
        """
        self.assertIsInstance(self.a, Review)

    def testHasAttributes(self):
        """
        Verify if attributes exist
        """
        self.assertTrue(hasattr(self.a, 'text'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'place_id'))
        self.assertTrue(hasattr(self.a, 'user_id'))

    def test_types(self):
        """
        Verify attributes types
        """
        self.assertIsInstance(self.a.place_id, str)
        self.assertIsInstance(self.a.user_id, str)
        self.assertIsInstance(self.a.text, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

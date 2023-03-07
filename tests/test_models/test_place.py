#!/usr/bin/python3
"""
Unitest for amenity
"""
import unitest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests instance and methods from amenity model
    """
    a = Place()

    def test_class_exists(self):
        """
        class exists
        """
        clss = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.a)), clss)

    def test_user_inheritance(self):
        """
        test if its a subclass of BaseModel
        """
        self.assertIsInstance(self.a, Place)

    def testHasAttributes(self):
        """
        Verify if attributes exist
        """
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'city_id'))
        self.assertTrue(hasattr(self.a, 'user_id'))
        self.assertTrue(hasattr(self.a, 'description'))
        self.assertTrue(hasattr(self.a, 'number_rooms'))
        self.assertTrue(hasattr(self.a, 'number_bathrooms'))
        self.assertTrue(hasattr(self.a, 'max_guest'))
        self.assertTrue(hasattr(self.a, 'price_by_night'))
        self.assertTrue(hasattr(self.a, 'latitude'))
        self.assertTrue(hasattr(self.a, 'longitude'))
        self.assertTrue(hasattr(self.a, 'amenity_ids'))

    def test_types(self):
        """
        Verify attributes types
        """
        self.assertIsInstance(self.a.city_id, str)
        self.assertIsInstance(self.a.user_id, str)
        self.assertIsInstance(self.a.description, str)
        self.assertIsInstance(self.a.number_rooms, int)
        self.assertIsInstance(self.a.number_bathrooms, int)
        self.assertIsInstance(self.a.max_guest, int)
        self.assertIsInstance(self.a.price_by_night, int)
        self.assertIsInstance(self.a.latitude, float)
        self.assertIsInstance(self.a.longitude, float)
        self.assertIsInstance(self.a.amenity_ids, list)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

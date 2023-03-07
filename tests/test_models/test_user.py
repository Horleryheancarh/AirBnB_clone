#!/usr/bin/python3
"""
Unitest for amenity
"""
import unitest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests instance and methods from user model
    """
    a = User()

    def test_class_exists(self):
        """
        class exists
        """
        clss = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.a)), clss)

    def test_user_inheritance(self):
        """
        test if its a subclass of BaseModel
        """
        self.assertIsInstance(self.a, User)

    def testHasAttributes(self):
        """
        Verify if attributes exist
        """
        self.assertTrue(hasattr(self.a, 'first_name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'last_name'))
        self.assertTrue(hasattr(self.a, 'email'))
        self.assertTrue(hasattr(self.a, 'password'))

    def test_types(self):
        """
        Verify attributes types
        """
        self.assertIsInstance(self.a.email, str)
        self.assertIsInstance(self.a.last_name, str)
        self.assertIsInstance(self.a.password, str)
        self.assertIsInstance(self.a.first_name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

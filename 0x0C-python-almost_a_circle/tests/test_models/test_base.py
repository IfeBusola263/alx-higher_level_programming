''' This the test file for the
Base class and Rectangles class and subclass'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' This tests the class Base '''

    def setUp(self):
        ''' The set up method executes before any test is executed '''

        self.obj = Base()
        self.obj1 = Base()
        self.obj2 = Base(10)
        self.obj4 = Base()


    def test_base(self):
        ''' Unittest for the base class '''

        self.assertEqual(self.obj.id, 1)
        self.assertEqual(self.obj1.id, 2)
        self.assertEqual(self.obj2.id, 10)
        self.assertEqual(self.obj4.id, 3)

        with  self.assertRaises(ValueError):
            self.obj3 = Base(-1)

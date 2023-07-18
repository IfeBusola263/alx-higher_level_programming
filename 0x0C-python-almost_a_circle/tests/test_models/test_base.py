''' This the test file for the
Base class and Rectangles class and subclass'''


import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    ''' This tests the class Base '''

    def setUp(self):
        ''' The set up method executes before any test is executed '''

        self.obj = Base()
        self.obj1 = Base()
        self.obj2 = Base(10)
        self.obj4 = Base()
        self.obj5 = Base(6000)


    def test_base(self):
        ''' Unittest for the base class '''

        self.assertEqual(self.obj.id, 1)
        self.assertEqual(self.obj1.id, 2)
        self.assertEqual(self.obj2.id, 10)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(self.obj5.id, 6000)

        with  self.assertRaises(ValueError):
            self.obj3 = Base(-1)

        with  self.assertRaises(ValueError):
            self.obj3 = Base(-12000)

    def test_to_json_string(self):
        ''' Test for the static method to_json '''

        expect_string = '[{"height": 2, "id": 15, "width": 5, "x": 3, "y": 4}]'
        obj = Rectangle(5, 2, 3, 4, 15)
        dict_rep = obj.to_dictionary()
        json_rep = Base.to_json_string([dict_rep])
        self.assertEqual(json_rep, expect_string)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        with self.assertRaises(TypeError):
            js_rep = Base.to_json_string()

''' This is a test suite for the Square class '''


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):
    ''' The Test squares inherits from the unittest class
    to check specific behaviour of the class square, when instantiated
    with other methods '''

    def setUp(self):
        ''' setup method executes before any of the tests exectes '''

        Base._Base__nb_objects = 0

        self.s1 = Square(3)
        self.s2 = Square(4, 2)
        self.s3 = Square(3, 1, 2)
        self.s4 = Square(3, 1, 2, 10)
        self.s5 = Square(3, 0, 0, 6)
        self.s6 = Square(3, 1, 2)

    def tearDown(self):
        ''' executes after every test '''

        del self.s1
        del self.s2
        del self.s3
        del self.s4
        del self.s5
        del self.s6

    def test_square(self):
        ''' Test for the instantiation of the square object '''

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)
        self.assertEqual(self.s5.id, 6)
        self.assertEqual(self.s6.id, 4)

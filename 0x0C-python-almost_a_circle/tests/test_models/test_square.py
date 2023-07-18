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

        with self.assertRaises(ValueError):
            self.obj = Square(2, 0, 0, -10)

        with self.assertRaises(TypeError):
            self.obj = Square()

    def test_size(self):
        ''' test for the behaviour of the size field
        The size field is not an attribute of the square,
        it basically just sets the width attribute of the
        square, since a square is kind of rectangle '''

        self.assertEqual(self.s1.width, 3)
        self.assertEqual(self.s2.width, 4)
        self.assertEqual(self.s3.width, 3)
        self.assertEqual(self.s4.size, 3)
        self.assertEqual(self.s4.width, 3)
        self.assertEqual(self.s5.width, 3)
        self.assertEqual(self.s6.width, 3)
        self.assertEqual(self.s6.size, 3)


        with self.assertRaises(ValueError):
            self.obj = Square(-10, 0, 0, 10)

        with self.assertRaises(ValueError):
             Square(0, 0, 0, 10)

        with self.assertRaises(TypeError):
             Square([3, 5], 0, 0, 10)

        with self.assertRaises(TypeError):
             Square((10,4), 0, 0, 10)

        with self.assertRaises(TypeError):
             Square("Hi", 0, 0, 10)

        with self.assertRaises(TypeError):
             Square(10.4, 0, 0, 10)

    def test_x(self):
        ''' Test for the x attribute '''

        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s4.x, 1)

        with self.assertRaises(ValueError):
             Square(10,-10, 0, 10)

        with self.assertRaises(TypeError):
             Square(6, [3, 5], 0, 10)

        with self.assertRaises(TypeError):
             Square(7, (10,4), 0, 10)

        with self.assertRaises(TypeError):
             Square(89, "Hi", 0, 10)

        with self.assertRaises(TypeError):
             Square(10, 5.2, 0, 10)

    def test_y(self):
        ''' Test for the y attribute '''

        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s4.y, 2)

        with self.assertRaises(ValueError):
             Square(10, 0, -10, 10)

        with self.assertRaises(TypeError):
             Square(6, 0, [3, 5], 10)

        with self.assertRaises(TypeError):
             Square(7, 2, (10,4), 10)

        with self.assertRaises(TypeError):
             Square(89, 6, "Hi", 10)

        with self.assertRaises(TypeError):
             Square(10, 6, 5.2, 10)

    def test_area(self):
        ''' Test for the area method in Rectangle class '''

        self.assertEqual(self.s1.area(), 9)
        self.assertEqual(self.s2.area(), 16)

    def test_display(self):
        ''' Tests the output for output of the rectangle '''

        # first check without padding
        expecting = "###\n###\n###"

        captured = StringIO()
        sys.stdout = captured

        self.s1.display()

        output_displayed = captured.getvalue().strip()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_displayed, expecting)

        # The second check for padding
        expected = "\n\n ###\n ###\n ###\n"

        capture = StringIO()
        sys.stdout = capture

        self.s3.display()

        output_display = capture.getvalue()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_display, expected)

    def test_str(self):
        ''' test for the magic print '''

        expected = "[Square] (3) 1/2 - 3"

        captured = StringIO()
        sys.stdout = captured

        print(self.s3)

        output_displayed = captured.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_displayed, expected)

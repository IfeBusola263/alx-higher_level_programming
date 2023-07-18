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

    def test_update(self):
        ''' Test for the update method of the class '''

        self.s = Square(10, 10, 10, 10)


        self.s.update(89)
        self.assertEqual(self.s.id, 89)

        self.s.update()
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 10)
        self.assertEqual(self.s.x, 10)
        self.assertEqual(self.s.y, 10)

        self.s.update(89, 2, size=9, id=8)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.width, 2)

        self.s.update(89, 2, 3)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 2)
        self.assertEqual(self.s.x, 3)

        self.s.update(89, 2, 3, 4)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 2)
        self.assertEqual(self.s.x, 3)
        self.assertEqual(self.s.y, 4)

        self.s.update(x=1, size=2, y=3)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.width, 2)
        self.assertEqual(self.s.size, 2)
        self.assertEqual(self.s.x, 1)
        self.assertEqual(self.s.y, 3)

        with self.assertRaises(ValueError):
             self.s.update(10, 5, -10, 10)

        with self.assertRaises(ValueError):
             self.s.update(10, 5, 10, -10)

        with self.assertRaises(ValueError):
             self.s.update(10, -5, 10, 10)

        with self.assertRaises(ValueError):
             self.s.update(0, 0, 0, 10)

        with self.assertRaises(TypeError):
             self.s.update(6, [5], 3, 10)

        with self.assertRaises(TypeError):
             self.s.update(7, 15, (10,4), 10)

        with self.assertRaises(TypeError):
             self.s.update(89, "Hi", 6, 10)

        with self.assertRaises(TypeError):
             self.s.update(10, 12.6, 5, 10)

        self.s6.update(size=5)
        self.assertEqual(self.s6.width, 5)

        self.s6.update(size=5, x=15)
        self.assertEqual(self.s6.size, 5)
        self.assertEqual(self.s6.width, 5)
        self.assertEqual(self.s6.x, 15)

        self.s6.update(x=8, size=5, y=15)
        self.assertEqual(self.s6.width, 5)
        self.assertEqual(self.s6.y, 15)
        self.assertEqual(self.s6.x, 8)

        self.s6.update(x=8, size=5, id=21,  y=4)
        self.assertEqual(self.s6.width, 5)
        self.assertEqual(self.s6.x, 8)
        self.assertEqual(self.s6.id, 21)
        self.assertEqual(self.s6.y, 4)

        arg = (3, 2, 6, 45)
        arg2 = {'size': 10, 'id': 56, 'height': 5, 'x': 24, 'y': 27}

        self.s1.update(*arg, **arg2)
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s1.id, 3)
        self.assertEqual(self.s1.y, 45)



        def test_to_dictionary(self):
            ''' Test for the method 'to_dictionary' to
            confirm the expected behaviour '''
            expected = {'size': 3, 'id': 10, 'x': 1, 'y': 2}
            dic_rep = s4.to_dictionary()
            self.assertEqual(dic_rep, expected)

            expected2 = {'size': 4, 'x': 2, 'y': 0, 'id': 2}
            dic_rep = s2.to_dictionary()
            self.assertEqual(dic_rep, expected2)

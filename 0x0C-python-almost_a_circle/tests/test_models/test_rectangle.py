''' This is the test for rectangle class which inherits for the Base class '''


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    ''' The test suite for the rectangle class '''

    def setUp(self):
        ''' setup method executes before any of the tests exectes '''

        Base._Base__nb_objects = 0

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2 ,10)
        self.r3 = Rectangle(10, 2, 2, 2, 12)
        self.r4 = Rectangle(10, 5, 24, 27, 56)
        self.r5 = Rectangle(12, 5, 0, 0, 60)
        self.r6 = Rectangle(10, 6, 0, 0, 78)
        self.r7 = Rectangle(10, 5, 2, 12)

    def tearDown(self):
        ''' executes after every test '''
        del self.r1
        del self.r2
        del self.r3
        del self.r4
        del self.r5
        del self.r6
        del self.r7

    def test_rectangle(self):
        ''' This test check for the expected output when an
        instance of this class is created '''

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.id, 56)
        self.assertEqual(self.r5.id, 60)
        self.assertEqual(self.r6.id, 78)
        self.assertEqual(self.r7.id, 3)

        with self.assertRaises(ValueError):
            self.obj = Rectangle(10, 5, 0, 0, -10)

        with self.assertRaises(TypeError):
            self.obj = Rectangle()

    def test_width(self):
        ''' Test for the width attribute '''
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r5.width, 12)

        with self.assertRaises(ValueError):
            self.obj = Rectangle(-10, 5, 0, 0, 10)

        with self.assertRaises(ValueError):
             Rectangle(0, 5, 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle([3, 5], 3, 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle((10,4), 5, 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle("Hi", 5, 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(10.4, 5, 0, 0, 10)


    def test_height(self):
        ''' Test for the height attribute '''

        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r6.height, 6)

        with self.assertRaises(ValueError):
             Rectangle(10, -5, 0, 0, 10)

        with self.assertRaises(ValueError):
             Rectangle(10, 0, 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(6, [3, 5], 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(7, (10,4), 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(89, "Hi", 0, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(10, 5.2, 0, 0, 10)

    def test_x(self):
        ''' Test for the x attribute '''

        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r4.x, 24)

        with self.assertRaises(ValueError):
             Rectangle(10, 5, -10, 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(6, 10, [3, 5], 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(7, 10, (10,4), 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(89, 20, "Hi", 0, 10)

        with self.assertRaises(TypeError):
             Rectangle(10, 15, 5.2, 0, 10)

    def test_y(self):
        ''' Test for the y attribute '''

        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r4.y, 27)

        with self.assertRaises(ValueError):
             Rectangle(10, 5, 0, -10, 10)

        with self.assertRaises(TypeError):
             Rectangle(6, 5, 0, [3, 5], 10)

        with self.assertRaises(TypeError):
             Rectangle(7, 15, 2, (10,4), 10)

        with self.assertRaises(TypeError):
             Rectangle(89, 30, 6, "Hi", 10)

        with self.assertRaises(TypeError):
             Rectangle(10, 12, 6, 5.2, 10)

    def test_area(self):
        ''' Test for the area method in Rectangle class '''

        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r7.area(), 50)

    def test_display(self):
        ''' Tests the output for output of the rectangle '''

        # first check without padding
        expecting = "##########\n##########"

        captured = StringIO()
        sys.stdout = captured

        self.r1.display()

        output_displayed = captured.getvalue().strip()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_displayed, expecting)

        # The second check for padding
        expected = "\n\n  ##########\n  ##########\n"

        capture = StringIO()
        sys.stdout = capture

        self.r3.display()

        output_display = capture.getvalue()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_display, expected)

    def test_str(self):
        ''' test for the magic print '''

        expected = "[Rectangle] (12) 2/2 - 10/2"

        captured = StringIO()
        sys.stdout = captured

        print(self.r3)

        output_displayed = captured.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_displayed, expected)

    def test_update(self):
        ''' Test for the update method of the class '''

        self.r = Rectangle(10, 10, 10, 10)

        self.r.update(89)
        self.assertEqual(self.r.id, 89)

        self.r.update()
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 10)
        self.assertEqual(self.r.height, 10)
        self.assertEqual(self.r.x, 10)
        self.assertEqual(self.r.y, 10)

        self.r.update(89, 2, width=9, height=8)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)

        self.r.update(89, 2, 3)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)

        self.r.update(89, 2, 3, 4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)

        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 5)

        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 4)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 3)

        with self.assertRaises(ValueError):
             self.r.update(10, 5, 0, -10, 10)

        with self.assertRaises(ValueError):
             self.r.update(10, 5, 0, 10, -10)

        with self.assertRaises(ValueError):
             self.r.update(10, -5, 0, 10, 10)

        with self.assertRaises(ValueError):
             self.r.update(0, 5, 0, 0, 10)

        with self.assertRaises(TypeError):
             self.r.update(6, [5], 0, 3, 10)

        with self.assertRaises(TypeError):
             self.r.update(7, 15, 2, (10,4), 10)

        with self.assertRaises(TypeError):
             self.r.update(89, 30,"Hi", 6, 10)

        with self.assertRaises(TypeError):
             self.r.update(10, 12.6, 6, 5, 10)

        self.r6.update(width=5)
        self.assertEqual(self.r6.width, 5)

        self.r6.update(width=5, height=15)
        self.assertEqual(self.r6.width, 5)
        self.assertEqual(self.r6.height, 15)

        self.r6.update(x=8, width=5, height=15)
        self.assertEqual(self.r6.width, 5)
        self.assertEqual(self.r6.height, 15)
        self.assertEqual(self.r6.x, 8)

        self.r6.update(x=8, width=5, id=21, height=15, y=4)
        self.assertEqual(self.r6.width, 5)
        self.assertEqual(self.r6.height, 15)
        self.assertEqual(self.r6.x, 8)
        self.assertEqual(self.r6.id, 21)
        self.assertEqual(self.r6.y, 4)

        arg = (3, 2, 6, 5, 45)
        arg2 = {'width': 10, 'id': 56, 'height': 5, 'x': 24, 'y': 27}

        self.r1.update(*arg, **arg2)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.y, 45)



        def test_to_dictionary(self):
            ''' Test for the method 'to_dictionary' to
            confirm the expected behaviour '''
            expected = {'width': 10, 'id': 56, 'height': 5, 'x': 24, 'y': 27}
            dic_rep = r4.to_dictionary()
            self.assertEqual(dic_rep, expected)

            expected2 = {'width': 2, 'x': 0, 'y': 0, 'height': 10, 'id': 2}
            dic_rep = r2.to_dictionary()
            self.assertEqual(dic_rep, expected2)

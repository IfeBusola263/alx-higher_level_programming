''' This is a unittest file to test the function max_integer '''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' This is an object oriented approach to testing the function
    max_integer '''

    def test_max_integer(self):
        ''' This method test several edge cases for max integer '''

        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([6, 1, 2, 3]), 6)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, -2, 3]), 3)

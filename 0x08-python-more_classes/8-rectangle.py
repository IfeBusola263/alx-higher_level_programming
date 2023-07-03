#!/usr/bin/python3
''' This module defines a Rectangle class and the atrributes '''


class Rectangle:
    ''' A rectangle class that defines width and height attributes '''

    number_of_instances = 0
    print_symbol = "#"
    print_symbol = str(print_symbol)

    def __init__(self, width=0, height=0):
        ''' The init method is a class method that initializes
        once an instance of the class is created '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ''' The width method with the property decorator
        is a setter to protect the attribute of the fields of the class'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' The width method with the decorator width.setter is an attribute
        setter for the class rectangle '''

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        ''' The width method with the property decorator
        is a setter to protect the attribute of the fields of the class'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' The width method with the decorator width.setter is an attribute
        setter for the class rectangle '''

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Area method returns the area of a rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Perimeter class method returns perimeter of a rectangle object'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' The str method creates a string object from the object created'''

        if self.__width == 0 or self.__height == 0:
            # if any side is zero, it's empty then
            return ''
        else:
            # prints each building block of the rectangle
            return '\n'.join(''.join(
                str(self.print_symbol) for i in range(self.__width))
                             for j in range(self.__height))

    def __repr__(self):
        ''' returns the string representation for
        creating the instance of the rectangle '''
        return "Rectangle"+"("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        ''' initiates when the del function is called on the instance of
        the class '''
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    def __lt__(self, other):
        '''Return a boolean value 'True' if self is less than other,
        and False otherwise'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Return a boolean value 'True' if self is less than
        or equal to other, and False otherwise'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''Return a boolean value 'True' if self is greater than
        other, and False otherwise'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Return a boolean value 'True' if self is greater than
        or equal to other, and False otherwise'''
        return self.area() >= other.area()

    def __eq__(self, other):
        '''Return a boolean value 'True' if self is
        equal to other, and False otherwise'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Return a boolean value 'True' if self is
        not equal to other, and False otherwise'''
        return self.area() != other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Returns the bigger rectangle between rect_1 and rect_2. '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1 == rect_2:
            return rect_1
        else:
            return max(rect_1.area(), rect_2.area())

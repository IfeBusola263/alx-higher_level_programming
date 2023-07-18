#!/usr/bin/python3
""" This module implements classes
"""

from models.base import Base


class Rectangle(Base):
    ''' The rectangle class inherits for the Base class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The Init method initializes variables for the instance of
        the Class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' getter method for the width attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter method for the width attribute '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        ''' getter method for the height attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter method for the height attribute '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        ''' getter method for the x attribute '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter method for the x attribute '''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        ''' getter method for the x attribute '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter method for the height attribute '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        ''' The area method computes the area of the rectangle '''

        return self.__width * self.__height

    def display(self):
        ''' The display method, prints out the rectangle '''

        # Print the y axis padding
        if self.__y > 0:
            for i in range(self.__y):
                print()

        # Before printing the square, check for padding
        for i in range(self.__height):

            # If there's a padding value
            if self.__x > 0:
                for tab in range(self.__x):
                    print(' ', end='')

            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        ''' The str magic method prints an arbitrary output, to override
        the str method of the object of base class '''

        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        ''' The method re-assigns values to the class attribute '''

        if args:
            if len(args) == 1:
                self.id = args[0]

            elif len(args) == 2:
                self.id, self.width = args

            elif len(args) == 3:
                self.id, self.width, self.height = args

            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args

            elif len(args) == 5:
                self.id, self.width, self.height, self.x, self.y = args

        else:
            for key, value in kwargs.items():

                if key == 'height':
                    self.height = value

                if key == 'width':
                    self.width = value

                if key == 'x':
                    self.x = value

                if key == 'id':
                    self.id = value

                if key == 'y':
                    self.y = value
            # for key, value in self.__dict__.items():
            #     for key2, value2 in kwargs.items():
            #         if key2 in key:
            #             self.__dict__[key] = value2


    def to_dictionary(self):
        ''' Returns the dictionary of the class instance '''

        return self.__dict__

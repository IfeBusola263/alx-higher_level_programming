#!/usr/bin/python3
''' This module implements the square class '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' The square class inherits from the rectangle class
    that gives access to the methods of the rectangle class
    and also the base of the rectangle class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' The init method executes when the instance of this
        class(Square) is created and also initializes the fields '''

        self.size = size

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' The attribute getter for the size attribute '''

        return self.__size

    @size.setter
    def size(self, value):
        ''' The property setter for checking the parameters before
        assigning them to the attributes '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        ''' The str magic method returns a string representation of the use case
        of the attributes of the square class '''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        ''' The method re-assigns values to the class attribute '''

        if args:
            if len(args) == 1:
                self.id = args[0]

            elif len(args) == 2:
                self.id, self.size = args

            elif len(args) == 3:
                self.id, self.size, self.x = args

            elif len(args) == 4:
                self.id, self.width, self.x, self.y = args

        else:
            for key, value in kwargs.items():

                if key == 'size':
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value

                if key == 'id':
                    self.id = value

                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' Returns the dictionary of the class instance '''

        return self.__dict__

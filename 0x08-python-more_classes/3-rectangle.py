#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Class defining a rectangle with the following attributes:
    Width (type: integer) - private
    Height (integer) - private
    Includes getter and setter method for both
    """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional nil width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter for the width property """
        return self.__width

    @property
    def height(self):
        """ getter for the height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for the width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter for the height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the area
        I.E Width x Height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter
        I.E. Width + Width + Height + Height
        If width or height is 0, perimeter is automatically 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Represents the rectangle as a string, using #
        Equivalent to ___repr___ (before task 4)
        """
        if self.width == 0 or self.height == 0:
            return ''
        representation = ''
        for col in range(self.height):
            for row in range(self.width):
                representation += '#'
            if col != self.height - 1:
                representation += '\n'
        return representation

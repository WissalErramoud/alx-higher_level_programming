#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Class defining a rectangle with the following attributes:
    Width (type: integer) - private
    Height (integer) - private
    Includes getter and setter method for both
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiation with optional nil width and height """
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
        Represents the rectangle as a string, using #*
        *updated to use custom symbol
        defined in attribute print_symbol
        Equivalent to ___repr___*
        *before task 4
        """
        if self.width == 0 or self.height == 0:
            return ''
        representation = ''
        for col in range(self.height):
            for row in range(self.width):
                representation += str(self.print_symbol)
            if col != self.height - 1:
                representation += '\n'
        return representation

    def __repr__(self):
        """
        Return a string representation of the rectangle
        Can be evaluated to make an instance of the same rectangle
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Destructor method """
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

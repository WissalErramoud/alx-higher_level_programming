
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


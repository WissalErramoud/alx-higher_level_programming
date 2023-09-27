#!/usr/bin/python3
"""
Define a Square class representing a square shape with size,
area, and printing methods.
"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes a new Square instance with an optional size."""
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters,
        with an empty line if size is 0."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

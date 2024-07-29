#!/usr/bin/python3

"""Module that contains functions for text indentation"""

def print_square(size):
    """prints a square with "#"'s that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for _ in range(size):
            print("#" * size)

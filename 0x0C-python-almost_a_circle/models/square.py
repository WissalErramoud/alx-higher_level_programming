#!/usr/bin/python3
"""Creating a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defining square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Call the super class (Rectangle) with size as both width and
        height"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overload the __str__ method to return [Square] (<id>) <x>/<y> -
        <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    """Getting size of square"""
    def size(self):
        return self.width

    @size.setter
    """Setting size of square"""
    def size(self, value):
        self.width = value
        self.height = value


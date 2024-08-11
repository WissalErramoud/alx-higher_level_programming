#!/usr/bin/python3
"""Creating a Student class."""


class Student:
    """Defining the Student class."""

    def __init__(self, first_name, last_name, age):
        """Initializing a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the instance.
        
        Args:
            attrs (list): Optional list of attribute names to include.
        
        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__


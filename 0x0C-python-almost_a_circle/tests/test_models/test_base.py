#!/usr/bin/python3
"""Unit tests for models/base.py"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """Resetting the counter before each test"""
        Base._Base__nb_objects = 0  # Accessing the private class attribute

    def test_base_no_id(self):
        """Test Base object creation without providing an ID"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_with_id(self):
        """Test Base object creation with a provided ID"""
        b1 = Base(100)
        b2 = Base()
        b3 = Base(200)
        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 1)  # Since ID is not provided, it should be incremented from 0
        self.assertEqual(b3.id, 200)

    def test_base_mixed_id(self):
        """Test Base object creation with and without providing an ID"""
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        b4 = Base(150)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 150)
        self.assertEqual(b5.id, 3)

if __name__ == "__main__":
    unittest.main()


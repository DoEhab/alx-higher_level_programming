#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test for fun max_integer"""

    def test_empty_list(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_ascending_list(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unordered_list(self):
        my_list = [1, 3, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_single_item_list(self):
        my_list = [1]
        self.assertEqual(max_integer(my_list), 1)

    def test_empty_string(self):
        my_list = ""
        self.assertEqual(max_integer(my_list), None)

    def test_diff_type(self):
        my_list = [1.2, 3.5, 4, -7, 1]
        self.assertEqual(max_integer(my_list), 4)

    def test_first_num_list(self):
        my_list = [4, 2, 3, 1]
        self.assertEqual(max_integer(my_list), 4)

    def test_string(self):
        string = "Bird"
        self.assertEqual(max_integer(string), 'r')


if __name__ == '__main__':
    unittest.main()

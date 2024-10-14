#!/usr/bin/python3
# File: 1-my_list.py
"""define class my list"""


class MyList(list):
    """define public fun print sorted list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

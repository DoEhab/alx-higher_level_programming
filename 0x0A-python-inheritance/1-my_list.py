#!/usr/bin/python3
"""define class my list"""


class MyList(list):
    """define public fun print sorted list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

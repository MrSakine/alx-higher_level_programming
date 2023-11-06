#!/usr/bin/python3
"""
This module is about a class MyList that inherits from list
"""


class MyList(list):
    """
    My list class definition
    """

    def print_sorted(self):
        """
        Print my list element in sorted order
        """
        print(sorted(self))

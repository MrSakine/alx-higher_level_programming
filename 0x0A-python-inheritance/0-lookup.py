#!/usr/bin/python3
"""
<0-lookup.py> module
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Attributes:
        obj (any): The object

    Returns: a list
    """
    return dir(obj)

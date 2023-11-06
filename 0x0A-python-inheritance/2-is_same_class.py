#!/usr/bin/python3
"""
<2-is_same_class.py> module
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class ; otherwise False

    Attributes:
        obj (any): the object
        a_class (any): the class to check

    Returns: a bool
    """
    return (type(obj) is a_class)

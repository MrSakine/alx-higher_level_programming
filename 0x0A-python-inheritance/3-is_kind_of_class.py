#!/usr/bin/python3
"""
<3-is_kind_of_class.py> module
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Attributes:
        obj (any): the object
        a_class (any): the class to check

    Returns: a bool
    """
    return (isinstance(obj, a_class))

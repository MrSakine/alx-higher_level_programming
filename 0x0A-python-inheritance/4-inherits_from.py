#!/usr/bin/python3
"""
<4-inherits_from.py> module
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False

    Attributes:
        obj (any): the object
        a_class (any): the class to check

    Returns: a bool
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

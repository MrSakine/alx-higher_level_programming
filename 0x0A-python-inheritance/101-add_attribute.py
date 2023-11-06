#!/usr/bin/python3
"""
<101-add_attribute.py> module
"""


def add_attribute(a_class, name, value):
    """
    Adds a new attribute to an object if it's possible
    Raise a TypeError exception, with the message can't add
    new attribute if the object can't have new attribute

    Attributes:
    a_class (any): class to use
    name (any): attribute name
    value (any): attribute value
    """
    if (not hasattr(a_class, "__dict__")):
        raise TypeError("can't add new attribute")

    setattr(a_class, name, value)

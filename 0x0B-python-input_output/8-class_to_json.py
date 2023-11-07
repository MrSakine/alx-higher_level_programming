#!/usr/bin/python3
"""
A script that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Attributes:
        obj (any): instance of a Class
    """
    return (obj.__getattribute__("__dict__"))

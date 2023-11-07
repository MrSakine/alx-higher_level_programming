#!/usr/bin/python3
"""
A function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Attributes:
        my_obj (any): object to serialize
    """
    return (json.dumps(my_obj))

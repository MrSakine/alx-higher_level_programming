#!/usr/bin/python3
"""
This module is about adding 2 integers or floats together.
It will throw some errors the numbers aren't integers or floats
Use this to run
add_integer = __import__('0-add_integer').add_integer
add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Add two numbers together, throw errors if the type of
    a and bisn't integer or float

    Attributes:
        a (any): first number
        b (any): second number

    Returns:
        The sum of the 2 numbers
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

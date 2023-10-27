#!/usr/bin/python3
"""
This module is about square from a number
It will throw some errors if the number isn't
an integer or a float or is zero
Use this to run
print_square = __import__('4-print_square').print_square
print_square(size)
"""


def print_square(size):
    """
    Print square based on size, throw errors when
    - size isn't an integer or a float
    - size is a float and less than zero
    - size is an integer and less then zero

    Attributes:
        size (any): the size of the square

    Returns: None
    """
    if (not isinstance(size, int) and not isinstance(size, float)):
        raise TypeError("size must be an integer")
    elif ((isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        if (isinstance(size, float)):
            size = int(size)
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print("")

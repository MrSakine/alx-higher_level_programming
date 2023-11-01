#!/usr/bin/python3
"""
This module is about to print square from a number
It will throw some errors if the number isn't
an integer or a float or is zero
Use this to run
print_square = __import__('4-print_square').print_square
print_square(size)
"""


def max_integer(my_list=[]):
    if (len(my_list) <= 0):
        return (None)

    bigNumber = my_list[0]
    for i in my_list:
        if (i > bigNumber):
            bigNumber = i

    return (bigNumber)

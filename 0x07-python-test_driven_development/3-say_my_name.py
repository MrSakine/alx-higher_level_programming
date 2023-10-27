#!/usr/bin/python3
"""
This module is about printing name from firstname and lastname
It will throw some errors if firstname and lastname
aren't real strings
Use this to run
say_my_name = __import__('3-say_my_name').say_my_name
say_my_name(firstname, lastname)
"""


def say_my_name(first_name, last_name=""):
    """
    Print name by firstname and lastname, throw errors when
    - firstname isn't a real string
    - lastname isn't a real string

    Attributes:
        first_name (any): the string name
        last_name (:obj:`str`, optional): the lastname,
        empty string as default value

    Returns:
        A new string containing the firstname and lastname
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

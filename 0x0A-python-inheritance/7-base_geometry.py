#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """
    BaseGeometry class definition
    """

    def area(self):
        """
        Raise an exception with a custom message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(str(name)))
        elif (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(str(name)))
        else:
            return (None)

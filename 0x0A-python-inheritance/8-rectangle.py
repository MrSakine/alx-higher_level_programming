#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""

"""
Base geometry class import
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class definition
    """

    def __init__(self, width, height):
        """
        Initialisation of instance attributes, validate input through
        super function (integer_validator)

        Attributes:
            width (any): the width of the rectangle
            height (any): the height of the rectangle

        Returns: None
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__height = height
        self.__width = width

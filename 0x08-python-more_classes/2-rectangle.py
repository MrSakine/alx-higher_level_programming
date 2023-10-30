#!/usr/bin/python3
"""
This module defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class definition
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with given width and height
        Throw errors when width and height aren't integers or less than zero

        Attributes:
            width (:obj:`str`, optional): The width of the rectangle
            height (:obj:`str`, optional): The height of the rectangle

        Returns: None
        """
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        elif (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return (self.__width)

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """Set a new width of the rectangle"""
        self.__init__(value, self.height)

    @height.setter
    def height(self, value):
        """Set a new height of the rectangle"""
        self.__init__(self.width, value)

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if (self.width == 0 or self.height == 0):
            return (0)
        return ((self.width + self.height) * 2)

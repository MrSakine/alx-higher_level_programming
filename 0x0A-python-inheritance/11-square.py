#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)
"""

"""
Rectangle class import
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class definition
    """

    def __init__(self, size):
        super().integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        return (str(super().__str__()).replace("Rectangle", "Square"))

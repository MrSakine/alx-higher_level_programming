#!/usr/bin/python3
"""
This module defines a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class definition

    Attributes:
        number_of_instances (int): Number of instances of class Rectangle,
            default to zero
        print_symbol (any): symbol for string representation, default to #
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle with given width and height
        Throw errors when width and height aren't integers or less than zero

        Attributes:
            width (:obj:`str`, optional): The width of the rectangle
            height (:obj:`str`, optional): The height of the rectangle
            print_symbol (any): symbol for string representation,
            default to None

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
            Rectangle.number_of_instances += 1
            self.print_symbol = None

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

    def __str__(self) -> str:
        """Print the rectangle with the print symbol"""
        output = ""
        new_line_character = '\n'
        symbol = (Rectangle.print_symbol
                  if self.print_symbol is None
                  else self.print_symbol)
        if (self.width == 0 or self.height == 0):
            return (output)
        for i in range(self.height):
            for _ in range(self.width):
                output += str(symbol)
            if (i < (self.height - 1)):
                output += new_line_character
        # output = output[:len(output) - 1]
        return (output)

    def __repr__(self) -> str:
        """Returns the class represention of the instance"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """
        Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A class method that finds the biggest elements between 2 instances

        Attributes:
            rect_1 (any): first instance
            rect_2 (any): second instance

        Returns: The biggest instance based on the area
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if (area_1 > area_2):
                return (rect_1)
            elif (area_2 > area_1):
                return (rect_2)
            else:
                return (rect_1)

    @classmethod
    def square(cls, size=0):
        return (cls(width=size, height=size))

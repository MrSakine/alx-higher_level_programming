#!/usr/bin/python3
"""
A class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class definition
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        - Call the super class with id - this super call with
        use the logic of the __init__ of the Base class
        - Assign each argument width, height, x and y to the right attribute

        Attributes:
            width (any): the width of the rectangle
            height (any): the height of the rectangle
            x (any, optional): row position when printing rectangle
            y (any, optional): column position when printing rectangle
            id (any, optional): id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            The private attribute (__width) of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Raise:
            - TypeError is value is not an integer
            - ValueError is value is less than or equal to zero

        Attributes:
            value (any): the new value to set
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            The private attribute (__height) of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Raise:
            - TypeError is value is not an integer
            - ValueError is value is less than or equal to zero

        Attributes:
            value (any): the new value to set
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Get the x position of the rectangle

        Returns:
            The private attribute (__x) of the rectangle
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set the x position of the rectangle

        Raise:
            - TypeError is value is not an integer
            - ValueError is value is less than zero

        Attributes:
            value (any): the new value to set
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Get the y position of the rectangle

        Returns:
            The private attribute (__y) of the rectangle
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set the y position of the rectangle

        Raise:
            - TypeError is value is not an integer
            - ValueError is value is less than zero

        Attributes:
            value (any): the new value to set
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Get the area of the rectangle

        Returns:
            An integer that represents the area of the rectangle
        """
        return (self.width * self.height)

    def display(self):
        """
        Display the rectangle based on width, height, x and y and character #
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def __str__(self) -> str:
        """
        String representation of the rectangle

        Returns:
            A new string containing class attributes
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
                .format(str(self.id), self.x, self.y, self.width, self.height)
                )

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes based on
        *args (non-keyword arguments) or **kwargs (keyword arguments)

        Raise:
            - TypeError is value is not an integer
        """
        if (args is not None and len(args) > 0):
            i = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                if (
                    type(arg) is not int and (attrs[i] != "id") and arg is None
                ):
                    raise TypeError("{} must be an integer".format(attrs[i]))
                try:
                    setattr(self, attrs[i], arg)
                    i += 1
                except IndexError:
                    pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Convert class to dictionnary

        Returns:
            A new dictionnary containing the class attributes
        """
        attrs = ["id", "width", "height", "x", "y"]
        response = {}
        for attr in attrs:
            response[attr] = self.__getattribute__(attr)
        return (response)

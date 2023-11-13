#!/usr/bin/python3
"""
A class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class definition
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height.
        Width and height will be each assigned to size,
        raise the same errors as for the rectangle class
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
        Get the size of the square

        Returns:
            The private attribute (__size) of the square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Raise:
            - TypeError is value is not an integer
            - ValueError is value is less than or equal to zero

        Attributes:
            value (any): the new value to set
        """
        self.__init__(value, self.x, self.y, self.id)

    def __str__(self) -> str:
        """
        String representation of the square

        Returns:
            A new string containing class attributes
        """
        text = super().__str__().replace("Rectangle", "Square").split("-")
        return ((text[0] + "- " + str(self.height)))

    def update(self, *args, **kwargs):
        """
        Update the square attributes based on
        *args (non-keyword arguments) or **kwargs (keyword arguments)

        Raise:
            - TypeError is value is not an integer
        """
        if (args is not None and len(args) > 0):
            i = 0
            attrs = ["id", "size", "x", "y"]
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
        attrs = ["id", "size", "x", "y"]
        response = {}
        for attr in attrs:
            response[attr] = self.__getattribute__(attr)
        return (response)

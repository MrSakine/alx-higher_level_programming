#!/usr/bin/python3
"""
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def __str__(self) -> str:
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
                .format(str(self.id), self.x, self.y, self.width, self.height)
                )

    def update(self, *args, **kwargs):
        if (args is not None and len(args) > 0):
            i = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                if (type(arg) is not int and (attrs[i] != "id") and arg == None):
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
        attrs = ["id", "width", "height", "x", "y"]
        response = {}
        for attr in attrs:
            response[attr] = self.__getattribute__(attr)
        return (response)

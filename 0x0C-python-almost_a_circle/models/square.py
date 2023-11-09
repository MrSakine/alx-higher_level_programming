#!/usr/bin/python3
"""
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.__init__(value, self.x, self.y, self.id)

    def __str__(self) -> str:
        text = super().__str__().replace("Rectangle", "Square").split("-")
        return ((text[0] + "- " + str(self.height)))

    def update(self, *args, **kwargs):
        if (args is not None and len(args) > 0):
            i = 0
            attrs = ["id", "size", "x", "y"]
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
        attrs = ["id", "size", "x", "y"]
        response = {}
        for attr in attrs:
            response[attr] = self.__getattribute__(attr)
        return (response)

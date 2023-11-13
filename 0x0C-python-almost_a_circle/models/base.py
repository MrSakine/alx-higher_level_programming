#!/usr/bin/python3
"""
Base class module, this class is used by the other ones as parent
"""
import json
import turtle


class Base():
    """
    Number of objects at each new instance if id is None
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """
        If id is not None, assign the public instance attribute id
        with this argument value otherwise, increment __nb_objects
        and assign the new value to the public instance attribute id

        Attributes:
            id (any): id of the instance
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A static method to convert a list of dictionnaries to
        json representation

        Returns:
            A new string that represents the JSON structure
        """
        if (list_dictionaries is None or len(list_dictionaries) <= 0):
            return ("[]")
        return (json.dumps(list_dictionaries))

    def from_json_string(json_string):
        """
        Convert a JSON representation to JSON object

        Returns:
            A new string that represents the JSON structure in Python world
        """
        if (json_string is None):
            return ([])
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file as json representation
        """
        items = []
        name = "{}.json".format(cls.__name__)
        if (list_objs is not None):
            for item in list_objs:
                items.append(item.to_dictionary())

        with open(file=name, mode="w", encoding="utf-8") as file:
            file.write(Base.to_json_string(items))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a file as csv representation
        """
        items = []
        name = "{}.csv".format(cls.__name__)
        if (list_objs is not None):
            for item in list_objs:
                temp = []
                for _, j in item.to_dictionary().items():
                    temp.append(str(j))
                items.append(",".join(temp))

        with open(file=name, mode="w", encoding="utf-8") as file:
            if (len(items) == 0):
                file.write("[]")
            else:
                for item in items:
                    print(item, file=file)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance from a dictionnary

        Returns:
            The newly created instance of the class
        """
        dummy = (1, 1) if cls.__name__ == "Rectangle" else (1,)
        instance = cls(*dummy)
        cls.update(instance, **dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances of the class from a file
        named by the class name (<name>.json)

        Returns:
        - Empty list if the file is not found
        - Otherwise, a list of instances of the class
        """
        name = "{}.json".format(cls.__name__)
        data = ""
        try:
            with open(file=name, encoding="utf-8") as file:
                data = file.read()
            return [cls.create(**d) for d in cls.from_json_string(data)]
        except FileNotFoundError:
            return ([])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances of the class from a file
        named by the class name (<name>.csv)

        Returns:
        - Empty list if the file is not found
        - Otherwise, a list of instances of the class
        """
        name = "{}.csv".format(cls.__name__)
        data = ""
        attrs = []
        results = []
        try:
            with open(file=name, encoding="utf-8") as file:
                data = file.readlines()
            for i in data:
                temp = i.split(",")
                if len(temp) == 4:
                    attrs = ["id", "size", "x", "y"]
                else:
                    attrs = ["id", "width", "height", "x", "y"]
                j = 0
                response = {}
                for k in i.split(","):
                    response[attrs[j]] = int(k)
                    j += 1
                results.append(response)
            return [cls.create(**result) for result in results]
        except FileNotFoundError:
            return ([])

    def draw(list_rectangles, list_squares):
        """
        Draw rectangle or square from turtle module

        Attributes:
            list_rectangles (any): list of rectangles instances
            list_squares (any): list of squares instance
        """
        drawer = turtle.Turtle()
        for rectangle in list_rectangles:
            drawer.penup()
            drawer.goto(rectangle.x, rectangle.y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(rectangle.width)
                drawer.left(90)
                drawer.forward(rectangle.height)
                drawer.left(90)
        for square in list_squares:
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(square.width)
                drawer.left(90)
                drawer.forward(square.height)
                drawer.left(90)
        turtle.exitonclick()

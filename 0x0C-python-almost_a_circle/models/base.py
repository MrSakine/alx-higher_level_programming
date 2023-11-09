#!/usr/bin/python3
"""
Base class module, this class is used by the other ones as parent
"""
import json


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
    def create(cls, **dictionary):
        """
        Create a new instance from a dictionnary

        Returns:
            The newly created instance of the class
        """
        dummy = (1, 1)
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

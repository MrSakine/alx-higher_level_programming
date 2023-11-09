#!/usr/bin/python3
"""
"""
import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None or len(list_dictionaries) <= 0):
            return ("[]")
        return (json.dumps(list_dictionaries))

    def from_json_string(json_string):
        if (json_string is None):
            return ([])
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        items = []
        name = "{}.json".format(cls.__name__)
        if (list_objs is not None):
            for item in list_objs:
                items.append(item.to_dictionary())

        with open(file=name, mode="w", encoding="utf-8") as file:
            file.write(Base.to_json_string(items))

    @classmethod
    def create(cls, **dictionary):
        dummy = (1, 1)
        instance = cls(*dummy)
        cls.update(instance, **dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        name = "{}.json".format(cls.__name__)
        data = ""
        try:
            with open(file=name, encoding="utf-8") as file:
                data = file.read()
            return [cls.create(**d) for d in cls.from_json_string(data)]
        except FileNotFoundError:
            return ([])

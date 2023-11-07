#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student():
    """
    Student class definition
    """

    def __init__(self, first_name, last_name, age):
        """
        Instance initialisation with 3 public attributes

        Attributes:
            first_name (any): first_name of the student
            last_name (any): last name of the student
            age (any): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the json object representation of the class"""
        return (self.__getattribute__("__dict__"))

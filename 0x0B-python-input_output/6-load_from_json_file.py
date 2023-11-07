#!/usr/bin/python3
"""
A function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Returns a JSON string from json file

    Attributes:
        filename (any): name of the file
    """
    with open(file=filename, encoding="utf8") as file:
        return json.load(file)

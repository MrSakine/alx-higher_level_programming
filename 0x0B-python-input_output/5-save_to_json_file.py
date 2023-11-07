#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Attributes:
        my_obj (any): object to serialize
        filename (any): name of the file
    """
    with open(file=filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))

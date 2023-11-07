#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(file=filename, encoding="utf-8") as file:
        print(file.read())

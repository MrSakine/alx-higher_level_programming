#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written

    Attributes:
        filename (:obj:`str`, optional): name of the file
        text (:obj:`str`, optional): text to write

    Returns: int (number of characters written)
    """
    length = 0
    with open(file=filename, mode="w", encoding="utf-8") as file:
        length = file.write(text)

    return (length)

#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Attributes:
        filename (:obj:`str`, optional): name of the file
        text (:obj:`str`, optional): text to write

    Returns: int (number of characters written)
    """
    length = 0
    with open(file=filename, mode="a", encoding="utf-8") as file:
        length += file.write(text)

    return (length)

#!/usr/bin/python3
"""
A function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new line after the line that contains search_string

    Attributes:
        filename (:obj:`str`, optional): name of the file
        search_string (:obj:`str`, optional): string to look for
        new_string (:obj:`str`, optional): string to append
    """
    new_lines = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(new_lines)

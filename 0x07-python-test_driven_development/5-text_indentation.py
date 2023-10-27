#!/usr/bin/python3
"""
This module is about replace characters by line break in a text
It will throw some errors if the text isn't a string
Use this to run
text_indentation = __import__('5-text_indentation').text_indentation
text_indentation(".?:")
"""


def text_indentation(text):
    """
    Replace characters [., ?, :] by line break in a text,
    throw errors when
    - text isn't a string

    Attributes:
        text (any): the text to use

    Returns: None
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        j = text[i]
        print(j, end="")
        if (j in [".", "?", ":"]):
            print("\n")
            if ((i + 1) < len(text) and (text[i + 1] == " ")):
                i += 1
        i += 1

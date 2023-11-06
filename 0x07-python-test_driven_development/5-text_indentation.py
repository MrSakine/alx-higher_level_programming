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
    whitespace_count = 0
    while (
        whitespace_count < len(text) and
        text[whitespace_count] == ' '
    ):
        whitespace_count += 1

    while whitespace_count < len(text):
        print(text[whitespace_count], end="")
        if (
            text[whitespace_count] == "\n" or text[whitespace_count] in ".?:"
        ):
            if text[whitespace_count] in ".?:":
                print("\n")
            whitespace_count += 1
            while (
                whitespace_count < len(text) and text[whitespace_count] == ' '
            ):
                whitespace_count += 1
            continue
        whitespace_count += 1

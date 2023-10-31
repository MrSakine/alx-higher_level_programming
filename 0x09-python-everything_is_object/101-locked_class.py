#!/usr/bin/python3
"""
This module prevents the user from dynamically creating
new instance attributes, except if the new instance
attribute is called first_name
"""


class LockedClass:
    """
    Locked class definition that prevents dynamic attributes expect
    the first_name attribute
    """
    __slots__ = ["first_name"]

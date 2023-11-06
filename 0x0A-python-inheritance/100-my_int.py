#!/usr/bin/python3
"""
a class MyInt that inherits from int

- MyInt is a rebel
- MyInt has == and != operators inverted
"""


class MyInt(int):
    """
    My int class definition
    """

    def __eq__(self, value):
        """
        Equal magic operator

        Returns true if current instance and value are different
        otherwise false
        """
        return (super().__ne__(value))

    def __ne__(self, value):
        """
        Not equal magic operator

        Returns true if current instance and value are the same
        otherwise false
        """
        return (super().__eq__(value))

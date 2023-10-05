#!/usr/bin/python3
a = 1
b = 2
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    print("{0} + {1} = {2}".format(a, b, (a + b)))
    return (a + b)


if (__name__ == "__main__"):
    add(a=a, b=b)

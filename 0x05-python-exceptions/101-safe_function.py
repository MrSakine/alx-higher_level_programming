#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: " + str(e), file=sys.stderr)
        result = None
    return (result)

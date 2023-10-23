#!/usr/bin/python3
def safe_print_integer(value):
    printed = True
    try:
        i = int(value)
        print("{:d}".format(i))
    except Exception:
        printed = False
    return (printed)

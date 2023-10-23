#!/usr/bin/python3
def safe_print_integer(value):
    printed = True
    try:
        print("{:d}".format(int(value)))
    except Exception:
        printed = False
    return (printed)

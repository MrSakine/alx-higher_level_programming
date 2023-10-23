#!/usr/bin/python3
def safe_print_integer(value):
    printed = True
    try:
        if (isinstance(value, int)):
            i = int(value)
            print("{:d}".format(i))
        else:
            raise Exception()
    except Exception:
        printed = False
    return (printed)

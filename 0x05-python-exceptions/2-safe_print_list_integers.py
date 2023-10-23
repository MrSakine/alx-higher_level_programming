#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0
    error = None
    for i in range(x):
        try:
            if (type(my_list[i]) is int):
                j = int(my_list[i])
                print("{:d}".format(j), end="")
                printed_elements += 1
        except IndexError as e:
            error = e
    if (error is not None):
        raise IndexError("list index out of range")
    return (printed_elements)

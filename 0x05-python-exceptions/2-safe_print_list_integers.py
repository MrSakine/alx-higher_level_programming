#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0
    for i in range(x):
        try:
            j = int(my_list[i])
            print("{:d}".format(j), end="")
            printed_elements += 1
        except BaseException:
            pass
    print("")
    return (printed_elements)

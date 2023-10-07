#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) <= 0):
        return (None)

    bigNumber = 0
    for i in my_list:
        if (i > bigNumber):
            bigNumber = i

    return (bigNumber)

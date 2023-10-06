#!/usr/bin/python3
def max_integer(my_list=[]):
    if (not my_list):
        return None

    tmp = 0
    for i in my_list:
        if (i > tmp):
            tmp = i

    return (tmp)

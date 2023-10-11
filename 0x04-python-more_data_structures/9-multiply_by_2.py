#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = [i for i in a_dictionary.keys()]
    values = [j * 2 for j in a_dictionary.values()]
    return (dict(zip(keys, values)))

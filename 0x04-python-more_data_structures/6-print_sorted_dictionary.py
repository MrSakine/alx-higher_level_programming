#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted([i for i in a_dictionary.keys()])
    for key in keys:
        print("{0}: {1}".format(key, a_dictionary[key]))

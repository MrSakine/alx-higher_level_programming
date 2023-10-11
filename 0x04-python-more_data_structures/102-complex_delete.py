#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = [[i, j] for i, j in a_dictionary.items() if j == value]
    if (len(temp) > 0):
        for k in temp:
            if (a_dictionary.get(k[0])):
                del a_dictionary[k[0]]

    return (a_dictionary)

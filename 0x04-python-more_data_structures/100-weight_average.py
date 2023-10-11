#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) <= 0):
        return (0)

    quotients = [(i * j) for (i, j) in my_list]
    divisers = [j for (_, j) in my_list]
    return (sum(quotients) / sum(divisers))

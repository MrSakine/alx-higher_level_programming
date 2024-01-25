#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) > 0:
        size = len(list_of_integers)
        if size == 1:
            return list_of_integers[0]
        elif size == 2:
            return max(list_of_integers)
        else:
            mid = int(size / 2)
            current = list_of_integers[mid]
            left = list_of_integers[mid - 1]
            right = list_of_integers[mid + 1]

            if current > left and current > right:
                return current
            elif current < left:
                return find_peak(list_of_integers[:mid])
            else:
                return find_peak(list_of_integers[mid + 1:])

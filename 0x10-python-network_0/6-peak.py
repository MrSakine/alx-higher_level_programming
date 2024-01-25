#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) > 0:
        low, high = 0, len(list_of_integers) - 1

        while low < high:
            mid = (low + high) // 2
            current = list_of_integers[mid]
            next_element = list_of_integers[mid + 1]

            if current < next_element:
                low = mid + 1
            else:
                high = mid

        return list_of_integers[low]

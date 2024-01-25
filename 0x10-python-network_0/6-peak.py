#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    n = len(list_of_integers)
    return find_peak_util(list_of_integers, 0, n - 1, n)


def find_peak_util(list_of_integers, start, end, size):
    """
    Recursive method that handles the logic of find_peak method
    """
    if (start <= end):
        mid = start + (end - start) // 2
        current = list_of_integers[mid]
        left = list_of_integers[mid - 1]
        right = list_of_integers[mid + 1]

        if (mid == 0 or left <= current and current >= right):
            return current

        if left > current:
            return find_peak_util(list_of_integers, start, mid - 1, size)
        return find_peak_util(list_of_integers, mid + 1, end, size)

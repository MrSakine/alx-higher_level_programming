#!/usr/bin/python3
def print_last_digit(number):
    f_number = number
    if (number < 0):
        f_number = -number
    last_digit = (f_number % 10)
    print("{0}".format(last_digit), end="")
    return (last_digit)

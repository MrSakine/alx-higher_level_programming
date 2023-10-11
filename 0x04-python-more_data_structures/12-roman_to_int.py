#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string or roman_string is None):
        return (0)
    romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    currentRomain = None
    nextRomain = None
    n = len(roman_string)
    i, a, b = 0, 0, 0
    while (i < n):
        currentRomain = list(filter(lambda x: x == roman_string[i], romains))
        if (len(currentRomain) == 0):
            res = 0
            break
        a = romains.get(currentRomain[0])
        if (i + 1 < n):
            nextRomain = list(
                filter(lambda y: y == roman_string[i + 1], romains))
            b = romains.get(nextRomain[0])

            if (a >= b):
                res += a
                i += 1
            else:
                res += (b - a)
                i += 2
        else:
            res += a
            i += 1

    return (res)

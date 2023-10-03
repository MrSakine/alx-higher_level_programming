#!/usr/bin/python3
for i in range(122, 96, -1):
    c = chr(i if i % 2 == 0 else i - 32)
    print("{0}".format(c), end="")

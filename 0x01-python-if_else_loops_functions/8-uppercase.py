#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        if ((x >= 32 and x <= 90) or (i >= '0' and i <= '9')):
            a = x
        else:
            a = ord(i) - 32
        b = chr(a)
        print("{0}".format(b), end="")
    print("{0}".format("\n"), end="")

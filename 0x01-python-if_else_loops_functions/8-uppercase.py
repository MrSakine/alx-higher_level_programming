#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        if ((x >= 65 and x <= 90) or (x == 32 or (i >= '0' and i <= '9'))):
            a = x
        else:
            a = ord(i) - 32
        b = chr(a)
        print(b, end="")
    print("\n", end="")

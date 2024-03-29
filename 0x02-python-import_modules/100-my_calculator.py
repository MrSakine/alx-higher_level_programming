#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv) - 1

    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = argv[argc - 2]
    b = argv[argc]
    operator = argv[argc - 1]
    result = 0
    a = int(a)
    b = int(b)

    if operator == "+":
        result = add(a, b)
        print("{0} + {1} = {2}".format(a, b, result))
    elif operator == "-":
        result = sub(a, b)
        print("{0} - {1} = {2}".format(a, b, result))
    elif operator == "*":
        result = mul(a, b)
        print("{0} * {1} = {2}".format(a, b, result))
    elif operator == "/":
        result = div(a, b)
        print("{0} / {1} = {2}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

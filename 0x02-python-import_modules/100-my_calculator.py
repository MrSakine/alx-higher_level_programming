#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv) - 1

    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    left = argv[argc - 2]
    right = argv[argc]
    operator = argv[argc - 1]
    res = 0
    left = int(left)
    right = int(right)

    match (operator):
        case "+":
            res = add(left, right)
            print("{0} + {1} = {2}".format(left, right, res))
        case "-":
            res = sub(left, right)
            print("{0} - {1} = {2}".format(left, right, res))
        case "*":
            res = mul(left, right)
            print("{0} * {1} = {2}".format(left, right, res))
        case "/":
            res = div(left, right)
            print("{0} / {1} = {2}".format(left, right, res))
        case _:
            res = -1
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

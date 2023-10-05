#!/usr/bin/python3
import sys


def command_line_addition(input: list[str] = []):
    """My command line addition function

        Args:
            input: list of strings
        Returns: None
    """
    if (len(input) <= 1):
        print("0")
    else:
        argc = (len(input) - 1)
        sumOfNumber: int = 0
        for i in range(1, argc + 1):
            try:
                temp = int(str(input[i]))
                sumOfNumber += temp
            except Exception:
                pass

        print(sumOfNumber)


if (__name__ == "__main__"):
    command_line_addition(input=sys.argv)

#!/usr/bin/python3
import sys


if (__name__ == "__main__"):
    argv = sys.argv
    if (len(argv) <= 1):
        print("0 arguments.")
    else:
        argc = (len(argv) - 1)
        plural = "argument" if argc == 1 else "arguments"
        print("{0} {1}:".format(argc, plural))

        for i in range(1, argc + 1):
            print("{0}: {1}".format((i), argv[i]))

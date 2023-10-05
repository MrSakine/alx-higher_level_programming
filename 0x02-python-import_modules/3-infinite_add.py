#!/usr/bin/python3
import sys

if (__name__ == "__main__"):
    sumOfNumber = 0
    
    for i in range(len(sys.argv) - 1):
        sumOfNumber += int(sys.argv[i + 1])
        
    print(sumOfNumber)

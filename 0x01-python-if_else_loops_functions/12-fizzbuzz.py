#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        a = "Buzz"
        if (i % 15 == 0):
            a = "FizzBuzz"
        elif (i % 3 == 0):
            a = "Fizz"
        elif (i % 5 == 0):
            a = "Buzz"
        else:
            a = i

        print("{0}".format(a), end=" ")

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    tmp = [j for j in matrix]
    if (len(tmp) > 0):
        for i in tmp:
            print(*i)
    else:
        print("")

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list([k ** 2 for k in x]), [i for i in matrix]))

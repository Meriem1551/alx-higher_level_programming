#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new += [list(map(lambda n: n ** 2, matrix[i]))]
    return (new)

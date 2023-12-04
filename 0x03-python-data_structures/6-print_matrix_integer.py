#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix = None:
        print(None)
    else:
        for row in matrix:
            for i in range(len(row)):
                print("{:d} ".format(row[i]), end="")

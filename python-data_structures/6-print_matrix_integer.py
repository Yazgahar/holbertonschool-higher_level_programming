#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in range(len(row)):
            print("{:d}".format(row[n]), end=' ' if n != len(row) - 1 else '')
        print()

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    my_matrix = []
    for col in matrix:
        output = list(map(lambda x: x**2, col))
        my_matrix.append(output)
    return my_matrix

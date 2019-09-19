#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        if isinstance(matrix, list):
            if all(isinstance(elem, list) for elem in matrix):
                return [[i * i for i in row] for row in matrix]

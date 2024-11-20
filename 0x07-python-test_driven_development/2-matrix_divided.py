#!/usr/bin/python3

def matrix_divided(matrix, div):
    row_size = len(matrix[0])
    new_matrix = []
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix

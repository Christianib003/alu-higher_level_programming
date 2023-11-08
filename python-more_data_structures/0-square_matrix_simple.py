#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for mat in matrix:
        matr = []
        i = 0
        while i < len(mat):
            matr.append(mat[i] ** 2)
            i += 1
        new_matrix.append(matr)
    return new_matrix

#!/usr/bin/python3
"""
Task 0. Rotate 2D Matrix

Rotate an n by n matrix
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix

    Takes an n by n matrix and rotates the matrix by
    90* clockwise.

    Arguments:
        matrix (List[n][n]): The matrix to rotate by 90*.
    """
    size = len(matrix)
    temp = [[x for x in row] for row in matrix]
    for k in range(size):
        for l in range(size):
            matrix[l][size-1-k] = temp[k][l]

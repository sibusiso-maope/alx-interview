#!/usr/bin/python3
'''2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90° clockwise
    Returns: Nothing'''
    left, right = 0, len(matrix) - 1

    while left < right:
        for k in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + k]
            # move bottom left to top left
            matrix[top][left + k] = matrix[bottom - k][left]
            # move bottom right to bottom left
            matrix[bottom - k][left] = matrix[bottom][right - k]
            # move top right to bottom right
            matrix[bottom][right - k] = matrix[top + k][right]
            # move top left to top right
            matrix[top + k][right] = topLeft
        right -= 1
        left += 1

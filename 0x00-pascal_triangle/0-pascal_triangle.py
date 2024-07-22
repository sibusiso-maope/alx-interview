#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    i = []
    if n <= 0:
        return i
    i = [[1]]
    for k in range(1, n):
        temp = [1]
        for l in range(len(i[k - 1]) - 1):
            curr = i[k - 1]
            temp.append(i[k - 1][l] + i[k - 1][l + 1])
        temp.append(1)
        i.append(temp)
    return i

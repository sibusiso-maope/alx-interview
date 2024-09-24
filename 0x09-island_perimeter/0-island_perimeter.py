#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for k, row in enumerate(grid):
        m = len(row)
        for l, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                k == 0 or (len(grid[k - 1]) > l and grid[k - 1][l] == 0),
                l == m - 1 or (m > l + 1 and row[l + 1] == 0),
                k == n - 1 or (len(grid[k + 1]) > l and grid[k + 1][l] == 0),
                l == 0 or row[l - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter

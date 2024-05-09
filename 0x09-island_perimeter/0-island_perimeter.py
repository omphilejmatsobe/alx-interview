#!/usr/bin/python3
"""
Module that returb perimeter of an island grid
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """

    hor = len(grid[0])
    ver = len(grid)
    edges = 0
    size = 0

    for i in range(ver):
        for j in range(hor):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2

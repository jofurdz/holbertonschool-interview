#!/usr/bin/python3
"""module contains function island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                perimeter += [grid[row + 1][column],
                              grid[row - 1][column],
                              grid[row][column - 1],
                              grid[row][column + 1]
                              ].count(0)
    return perimeter

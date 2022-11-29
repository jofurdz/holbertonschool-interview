#!/usr/bin/python3
"""module contains function island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                newList = []
                if row == 0:
                    newList.append(0)
                else:
                    newList.append(grid[row - 1][column])
                if column == 0:
                    newList.append(0)
                else:
                    newList.append(grid[row][column - 1])
                perimeter += newList.count(0)
    return perimeter * 2

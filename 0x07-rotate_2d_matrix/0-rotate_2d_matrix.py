#!/usr/bin/python3
"""module containing function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    N = len(matrix)
    for row in range(N):
        new = []
        for col in range(N - 1, -1, -1):
            new.append(matrix[col][row])
        matrix.append(new)
    [matrix.pop(0) for i in range(N)]

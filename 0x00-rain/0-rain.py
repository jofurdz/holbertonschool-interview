#!/usr/bin/env python3
"""module containing function rain"""


def rain(walls):
    """calculates how much water will be retained after it rains"""
    water = 0

    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water += (min(left, right) - walls[i])

    return water

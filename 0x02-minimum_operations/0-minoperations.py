#!/usr/bin/python3
"""function for finding the minimum number of operations
to result in exactly n H characters in the file"""
import sys


def minOperations(n):
    """minimum operations to find nH characters in file"""
    minOp, div = 0, 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minOp += div
        n = int(n / div)
    return minOp

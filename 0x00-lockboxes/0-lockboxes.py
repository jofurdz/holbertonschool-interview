#!/usr/bin/env python3
"""module that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if boxes can be opened"""
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for row in range(1, len(boxes) - 1):
        newList = False
        for column in range(len(boxes)):
            newList = row in boxes[column] and row != column
            if newList:
                break
        if newList is False:
            return newList
    return True

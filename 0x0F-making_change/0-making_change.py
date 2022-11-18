#!/usr/bin/python3
"""contains function makeChange"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount"""
    """if total <= 0:
        return 0

    count = 0
    #for coin in coins:
    maxCoin = max(coins)
    while maxCoin <= total:
        total -= maxCoin
        count += 1
    coins.remove(maxCoin)
    if total <= 0:
        return -1
    else:
        return count"""
    if total < 1:
        return 0
    change = 0
    coins.sort(reverse=True)
    for coin in coins:
        temp_change = int(total / coin)
        total -= (temp_change * coin)
        change += temp_change
        if total == 0:
            return change
    if total != 0:
        return -1

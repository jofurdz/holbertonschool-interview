#!/usr/bin/python3
"""function for finding the minimum number of operations
to result in exactly n H characters in the file"""
import sys


def minOperations(n):
    """minimum operations to find nH characters in file"""
    dp = [sys.maxsize] * (n + 1)
     
    # Initial state
    dp[1] = 0
     
    # Iterate for the remaining numbers
    for i in range(2, n + 1):
         
        # If the number can be obtained
        # by multiplication by 2
        if i % 2 == 0:
            x = dp[i // 2]
            if x + 1 < dp[i]:
                dp[i] = x + 1
         
        # If the number can be obtained
        # by multiplication by 3
        if i % 3 == 0:
            x = dp[i // 3]
            if x + 1 < dp[i]:
                dp[i] = x + 1
                 
        # Obtaining the number by adding 1
        x = dp[i - 1]
        if x + 1 < dp[i]:
            dp[i] = x + 1
             
    # Return the minimum operations
    # to obtain n
    return dp[n]
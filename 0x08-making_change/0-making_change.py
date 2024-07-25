#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins needed
to meet a given total amount from a list of coin denominations.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to reach.

    Returns:
        int: Fewest number of coins needed to meet the total,
        or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize DP array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

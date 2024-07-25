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
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1

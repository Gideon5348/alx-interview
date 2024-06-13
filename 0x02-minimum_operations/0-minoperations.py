#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to
    result in exactly n H characters in the file.

    :param n: Number of H characters desired.
    :type n: int
    :return: Minimum number of operations.
    :rtype: int
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

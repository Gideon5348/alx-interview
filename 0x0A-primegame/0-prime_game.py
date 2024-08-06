#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game played by Maria and Ben.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the end number for each round.

    Returns:
        str: Name of the player with the most wins, or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n > 1:
            if play_game(n, primes):
                maria_wins += 1
            else:
                ben_wins += 1
        else:
            ben_wins += 1  # Ben wins if n <= 1 because Maria cannot make a move

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve(n):
    """
    Use the Sieve of Eratosthenes to find all primes up to n.

    Args:
        n (int): The upper limit to find primes.

    Returns:
        list: List of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

def play_game(n, primes):
    """
    Simulate the game for a single round.

    Args:
        n (int): The upper limit of the numbers in the game.
        primes (list): List of prime numbers up to the maximum number in the game.

    Returns:
        bool: True if Maria wins, False if Ben wins.
    """
    taken = set()
    moves = 0

    for p in primes:
        if p > n:
            break
        if p not in taken:
            moves += 1
            for multiple in range(p, n + 1, p):
                taken.add(multiple)

    return moves % 2 == 1

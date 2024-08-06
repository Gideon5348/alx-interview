#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game played by Maria and Ben.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers rep the end number for each round.

    Returns:
        str: Name of the player with the most wins, or None if it's a tie.
    """
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
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    def play_game(n):
        """
        Simulate the game for a single round.

        Args:
            n (int): The upper limit of the numbers in the game.

        Returns:
            bool: True if Maria wins, False if Ben wins.
        """
        primes = sieve(n)
        moves = 0
        taken = set()

        for p in primes:
            if p not in taken:
                moves += 1
                for multiple in range(p, n + 1, p):
                    taken.add(multiple)

        return moves % 2 == 1  # True if Maria wins, False if Ben wins

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

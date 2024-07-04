#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    """Check if a queen can be placed on board at row, col"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def solve(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    solve(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

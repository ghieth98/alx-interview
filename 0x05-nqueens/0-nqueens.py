#!/usr/bin/python3
""" Module N Queens
"""
import sys


def solveNQueens(n: int):
    """
    Finds all valid arrangements of `n` queens on an `n x n` chessboard.
    """

    def DFS(queens, xy_dif, xy_sum):
        """
        Performs a depth-first search to find all valid queen arrangements.
        """
        r = len(queens)
        if r == n:
            solutions.append(queens)
            return None

        for c in range(n):
            if c not in queens and r - c not in xy_dif and r + c not in xy_sum:
                DFS(queens + [c], xy_dif + [r - c], xy_sum + [r + c])

    solutions = []
    DFS([], [], [])

    return solutions


def main():
    """ Main
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solveNQueens(N):
        print([[i, j] for i, j in enumerate(solution)])


if __name__ == "__main__":
    main()

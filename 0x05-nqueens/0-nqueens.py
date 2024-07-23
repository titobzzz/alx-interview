#!/usr/bin/python3
"""N-queens solution finder module."""
import sys

def get_input():
    """Retrieves & validates this program's argument.
    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.
    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in attacking position, else False.
    """
    return (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]) or \
           (abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))

def solve_nqueens(n):
    """Solve the N-queens problem and print the solutions."""
    def place_queen(queens, row):
        if row == n:
            print([[i, queens[i]] for i in range(n)])
            return
        for col in range(n):
            if all(not is_attacking([row, col], [i, queens[i]]) for i in range(row)):
                queens[row] = col
                place_queen(queens, row + 1)

    place_queen([0] * n, 0)

if __name__ == "__main__":
    n = get_input()
    solve_nqueens(n)
    
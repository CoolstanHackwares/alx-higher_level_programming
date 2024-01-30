#!/usr/bin/python3
"""
Nqueens program utilizing backtracking to print the
coordinates of nqueens on a nxn grid
"""


from sys import argv

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, n):
    if row == n:
        # Found a solution, print it
        for i in range(n):
            for j in range(n):
                print("Q" if board[i][j] == 1 else ".", end=" ")
            print()
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0  # Backtrack

def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./nqueens_alternative.py N")
        exit(1)

    try:
        N = int(argv[1])
        if N < 4:
            print("N must be at least 4")
            exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        exit(1)

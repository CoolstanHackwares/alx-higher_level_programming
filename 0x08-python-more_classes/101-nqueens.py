#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = 0  
try:
    N = int(sys.argv[1]) 
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4") 
    sys.exit(1)

solutions = []

def is_valid(col_positions):
    current_row = len(col_positions)
    for row in range(current_row):
        if abs(col_positions[row] - col_positions[current_row]) in (0, current_row - row):
            return False
    return True

def search(col_positions=[]):
    if len(col_positions) == N:  
        solutions.append(col_positions)
        return

    for col in range(N):
        col_positions.append(col)
        if is_valid(col_positions):
            search(col_positions.copy())  
        col_positions.pop()

search()

for solution in solutions:
    print([["{}{}".format(row, col) for col in solution]])

#!/usr/bin/python3
import sys

def print_solution(solution):
    print([[f"{row}{col}"  for col in solution]])

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)


    solutions = []

    def is_valid(col_positions):

        def search(col_positions=[]):
            if len(col_positions) == N:
                solutions.append(col_positions)
            return

        for col in range(N):


            search()

    for solution in solutions:
        print_solution(solution)    for col in range(N):
            # Recursive search logic

    search()

    # Print each solution  
    for solution in solutions:
        print_solution(solution)

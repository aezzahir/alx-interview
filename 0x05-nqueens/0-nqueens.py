#!/usr/bin/python3
import sys

# Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Convert the command-line argument to an integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is within the valid range
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

def is_safe(board, row, col, N):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    # Base case: If all queens are placed, return True
    if col == N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nqueens(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

def nqueens(N, i):
    # Create a 2D list to represent the board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Call the recursive function to solve the N-Queens problem
    solve_nqueens(board, i, N)

    # Construct the list of solution representations
    solutions = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution = []
                for k in range(N):
                    for l in range(N):
                        if board[k][l] == 1:
                            solution.append([k, l])
                solutions.append(solution)
                print(solution)

    return solutions

for i in range(N):
    print(nqueens(N, i))
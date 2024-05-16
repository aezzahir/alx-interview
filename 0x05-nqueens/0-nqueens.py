#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on the board[row][col]
    """
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


def solve_nqueens(board, col, N, solutions):
    """
    Recursive function to solve the N Queens problem
    """
    # Base case: If all queens are placed, add the solution to the list
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Consider this column and try placing this queen in all rows
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, N, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove the queen from board[i][col]
            board[i][col] = 0


def nqueens(N):
    """
    Main function to solve the N Queens problem
    """
    # Create a 2D list to represent the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    # Call the recursive function to solve the N-Queens problem
    solve_nqueens(board, 0, N, solutions)

    return solutions


if __name__ == "__main__":
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

    # Solve the N Queens problem
    solutions = nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)

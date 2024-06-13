#!/usr/bin/python3
"""
Function to calculate the perimeter of the island described in the grid.
"""


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Check each of the four sides
                if row == 0 or grid[row-1][col] == 0:  # Top side
                    perimeter += 1
                if row == rows-1 or grid[row+1][col] == 0:  # Bottom side
                    perimeter += 1
                if col == 0 or grid[row][col-1] == 0:  # Left side
                    perimeter += 1
                if col == cols-1 or grid[row][col+1] == 0:  # Right side
                    perimeter += 1

    return perimeter

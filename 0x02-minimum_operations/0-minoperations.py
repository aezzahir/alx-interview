#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """
    Minimum Operations 
    """
    if n <= 0:
        return 0
    result = "H"
    tmp = ""
    num_operations = 0
    while len(result) < n:
        if n % len(result) == 0:
            tmp = result
            result += tmp
            num_operations += 2
            continue
        elif n % len(result) != 0:
            result += tmp
            num_operations += 1
            continue
    if len(result) == n:
        return num_operations
    return 0

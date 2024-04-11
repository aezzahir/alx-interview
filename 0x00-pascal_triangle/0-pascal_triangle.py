#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(N):

    if N <= 0:
        return [[]]
    C = [[1]]
    for n in range(1, N):
        B = [1]
        for m in range(1, n):
            B.append(C[n - 1][m] + C[n - 1][m - 1])
        B.append(1)
        C.append(B)
    return C

#!/usr/bin/python3
"""
BFS Algorithm
"""


def canUnlockAll(boxes):
    """
    canUnlockAll function
    """
    n = len(boxes)
    visited = set()  # Set to store visited boxes
    queue = [0]      # Queue to keep track of boxes to visit

    while queue:
        box = queue.pop(0)
        visited.add(box)

        for key in boxes[box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
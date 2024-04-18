#!/usr/bin/python3
"""
BFS Algorithm
"""


def can_unlock_all(boxes):
    """
    Checks whether a series of locked boxes can be
    opened based on available keys.
    This function solves the lockboxes problem.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        box_checked = False
        for idx, box in enumerate(boxes):
            box_checked = key in box and key != idx
            if box_checked:
                break
        if not box_checked:
            return False
    return True

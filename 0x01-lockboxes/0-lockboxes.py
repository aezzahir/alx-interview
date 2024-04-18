from collections import deque

def canUnlockAll(boxes):
    """
    Determines whether all boxes can be opened based on keys found in boxes.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    opened_boxes = deque([0])

    while opened_boxes:
        current_box = opened_boxes.popleft()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                opened_boxes.append(key)

    return all(visited)

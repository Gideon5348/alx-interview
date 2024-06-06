#!/usr/bin/python3
"""
Module for checking if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of list of int): List of lists where each sublist contains keys
    to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]
    visited[0] = True
    opened_boxes = 1

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
                opened_boxes += 1

    return opened_boxes == n

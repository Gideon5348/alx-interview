#!/usr/bin/python3
def canUnlockAll(boxes):
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

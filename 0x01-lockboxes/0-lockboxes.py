#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set()
    to_visit = [0]

    while to_visit:
        box = to_visit.pop()
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key < n:
                    to_visit.append(key)

    return len(unlocked) == n


# Test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

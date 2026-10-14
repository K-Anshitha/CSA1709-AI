# Water Jug Problem using BFS
from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print("Jug 1:", jug1, "Jug 2:", jug2)

        if jug1 == target or jug2 == target:
            print("Target reached!")
            return

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (capacity2 - jug2)),
             min(capacity2, jug1 + jug2)),
            (min(capacity1, jug1 + jug2),
             max(0, jug2 - (capacity1 - jug1)))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Target cannot be reached.")

# Jug capacities and target
water_jug(4, 3, 2)

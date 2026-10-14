# Missionaries and Cannibals Problem using BFS
from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = {start}

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found:")
            for step, s in enumerate(path):
                print("Step", step, ":", s)
            return

        for dm, dc in moves:
            if boat == 1:
                nm, nc = m - dm, c - dc
                nb = 0
            else:
                nm, nc = m + dm, c + dc
                nb = 1

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3 - nm, 3 - nc

            if (nm > 0 and nm < nc) or (rm > 0 and rm < rc):
                continue

            new_state = (nm, nc, nb)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")

solve()

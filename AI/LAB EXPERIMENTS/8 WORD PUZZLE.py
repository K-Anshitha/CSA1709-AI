from collections import deque

# Initial state (0 represents the blank space)
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def solve(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

# Solve the puzzle
path = solve(start, goal)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i + 3])
else:
    print("No solution found.")

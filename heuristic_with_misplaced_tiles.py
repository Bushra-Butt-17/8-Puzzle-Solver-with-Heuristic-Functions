# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Heuristic function using misplaced tiles
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h


def solve_puzzle(initial_state):
    open_list = [(heuristic(initial_state), initial_state)]
    closed_set = set()

    while len(open_list) <= 1000:
        _, current_state = min(open_list)
        print("-->", current_state)
        if current_state == goal_state:
            return current_state

        closed_set.add(tuple(map(tuple, current_state)))

        # Generating possible next states
        for move in moves:
            new_state = [list(row) for row in current_state]
            blank_row, blank_col = None, None
            for i in range(3):
                for j in range(3):
                    if new_state[i][j] == 0:
                        blank_row, blank_col = i, j
                        break

            new_row, new_col = blank_row + move[0], blank_col + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[blank_row][blank_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[blank_row][blank_col],
                )
                if tuple(map(tuple, new_state)) not in closed_set:
                    open_list.append((heuristic(new_state), new_state))

    return None  # No solution


"""------------------------------------------------------------------------"""
initial_state = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
print("Heuristic of initial_state:", heuristic(initial_state))
print("STEPS:")

solution = solve_puzzle(initial_state)
if solution is not None:
    print("Solution:")
    for row in solution:
        print(row)
else:
    print("No solution exists.")

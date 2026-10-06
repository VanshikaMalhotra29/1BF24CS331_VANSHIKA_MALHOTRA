import heapq

START = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
)

GOAL = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# Manhattan Distance
def manhattan(state):
    distance = 0

    for i in range(9):

        # Don't count blank
        if state[i] == 0:
            continue

        # Current position
        current_row = i // 3
        current_col = i % 3

        # Goal position
        goal_index = GOAL.index(state[i])
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# Generate next states
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    for move in MOVES[blank]:

        new_state = list(state)

        new_state[blank], new_state[move] = \
            new_state[move], new_state[blank]

        neighbors.append(tuple(new_state))

    return neighbors


# A* Search
def a_star(start):

    # (f, g, state, path)
    priority_queue = []

    g = 0
    h = manhattan(start)
    f = g + h

    heapq.heappush(
        priority_queue,
        (f, g, start, [start])
    )

    visited = set()

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        # Goal reached
        if state == GOAL:
            return path

        # Generate children
        for next_state in get_neighbors(state):

            if next_state not in visited:

                new_g = g + 1
                new_h = manhattan(next_state)
                new_f = new_g + new_h

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        next_state,
                        path + [next_state]
                    )
                )

    return None


# Display puzzle
def display(state):

    for i in range(0, 9, 3):

        print(
            state[i],
            state[i + 1],
            state[i + 2]
        )

    print()


# Run A*
solution = a_star(START)

print("Initial State:")
display(START)

print("Solution:")

for step, state in enumerate(solution):

    print("Step", step)
    display(state)

print("Total moves:", len(solution) - 1)

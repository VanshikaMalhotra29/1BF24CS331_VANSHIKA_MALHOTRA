import heapq

# Initial and goal states
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

# Possible positions for blank (0)
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


# Misplaced Tiles heuristic
def h(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


# Generate next states
def successors(state):
    result = []

    blank = state.index(0)

    for move in MOVES[blank]:
        new_state = list(state)

        new_state[blank], new_state[move] = \
            new_state[move], new_state[blank]

        result.append(tuple(new_state))

    return result


# A* algorithm
def a_star(start):

    # (f, g, state, path)
    pq = []

    heapq.heappush(
        pq,
        (h(start), 0, start, [start])
    )

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        # Goal reached
        if state == GOAL:
            return path

        # Generate successors
        for next_state in successors(state):

            if next_state not in visited:

                new_g = g + 1
                new_h = h(next_state)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g,
                     next_state,
                     path + [next_state])
                )

    return None


# Display state
def display(state):
    print(
        state[0], state[1], state[2],
        sep="  "
    )
    print(
        state[3], state[4], state[5],
        sep="  "
    )
    print(
        state[6], state[7], state[8],
        sep="  "
    )
    print()


# Run A*
solution = a_star(START)

print("Initial State:")
display(START)

print("Solution:")

for i, state in enumerate(solution):
    print("Step", i)
    display(state)

print("Total moves:", len(solution) - 1)

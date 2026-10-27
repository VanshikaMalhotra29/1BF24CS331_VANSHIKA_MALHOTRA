import random

# Calculate the number of pairs of attacking queens
def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Queens attack diagonally if row difference
            # equals column difference
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Generate neighboring states by swapping two rows
def get_neighbors(state):
    neighbors = []
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = (
                new_state[j], new_state[i]
            )
            neighbors.append(new_state)

    return neighbors


# Hill Climbing algorithm
def hill_climbing():
    # Random initial state
    state = random.sample(range(4), 4)

    while True:
        current_cost = calculate_cost(state)

        print("State:", state, "Cost:", current_cost)

        # Goal state reached
        if current_cost == 0:
            print("Solution found:", state)
            return

        neighbors = get_neighbors(state)

        # Select the neighbor with minimum cost
        best_neighbor = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best_neighbor)

        # Stop if no improvement is possible
        if best_cost >= current_cost:
            print("Local minimum reached. Restarting...")
            state = random.sample(range(4), 4)
        else:
            state = best_neighbor


# Run the program
hill_climbing()


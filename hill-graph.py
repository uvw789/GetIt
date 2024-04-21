import numpy as np


def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape

    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))

    return neighbours


# Current optimization objective: local/global maximum
def hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
    for neighbour in neighbours: #Find the neighbour with the greatest value
        if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbour
            ascended = True

    return ascended, next_state


def __main__():
    landscape = np.random.randint(1,50,(10,10))
    print(landscape)
    start_state = (3, 6)  # matrix index coordinates
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ", landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ", landscape[current_state[0]][current_state[1]])


__main__()

# OUTPUT can vary bc random function is used
# [[23  3 15 32  8  6 42 36 30 31]
#  [23  9 48  1  7 22 30  1 41 13]
#  [33 31 39 32 44 34 42 19 48 47]
#  [25 29 43 34 37  7 37 12 37  2]
#  [24  3 39 42  8 16 31 35 14 28]
#  [49 33  6 22 31 26  1  6 11 35]
#  [12  9 11  8  8 12 45 41 29 32]
#  [18 21  7 41 28 28 11 23 47 28]
#  [12 46 10 18 31 33 18 45 32 32]
#  [49 39 20 18 47 24 30 11 23  2]]

# Step # 1
# Current state coordinates:  (3, 6)
# Current state value:  37

# Step # 2
# Current state coordinates:  (2, 6)
# Current state value:  42

# Step # 3
# Optimization objective reached.
# Final state coordinates:  (2, 6)
# Final state value:  42

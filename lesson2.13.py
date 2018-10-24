# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def mark_used(grid, move):
    grid[move[0]][move[1]] = 1


def mark_action(grid, move):
    grid[move[0]][move[1]] = move[3]


def possible_moves(grid, position):
    moves = []
    for i in range(len(delta)):
        move = delta[i]
        next_pos = [position[0] + move[0], position[1] + move[1], i]
        if min(next_pos) >= 0 \
                and next_pos[0] < len(grid) \
                and next_pos[1] < len(grid[1]) \
                and grid[next_pos[0]][next_pos[1]] is 0:
            moves.append(next_pos)

    return moves


def search(grid, init, goal, cost):
    open_list = [[0] + init + [-1]]
    actions = [[-1 for x in range(len(grid[0]))] for x in range(len(grid))]
    while len(open_list) > 0:
        # Take element with lowest G value
        move = min(open_list, key=lambda x: x[0])

        # Mark action
        actions[move[1]][move[2]] = move[3]

        # Check if we're done
        if move[1] is goal[0] and move[2] is goal[1]:
            break

        # Find possible moves
        moves = possible_moves(grid, move[1:3])

        # Set new G value
        moves = [[move[0] + cost] + x for x in moves]

        # check last move off and append new moves
        open_list += [x for x in moves if x not in open_list]
        open_list.remove(move)
        mark_used(grid, move[1:3])

    return create_path(actions, goal, init)


def create_path(actions, goal, init):
    # Empty path matrix
    path = [[' ' for x in range(len(actions[0]))] for x in range(len(actions))]
    path[goal[0]][goal[1]] = "*"

    # Fill the matrix
    current = [goal[0], goal[1]]
    while True:
        action = actions[current[0]][current[1]]
        move = delta[action]
        previous = [current[0] - move[0], current[1] - move[1]]
        path[previous[0]][previous[1]] = delta_name[action]
        current = previous

        # Python needs a do..while
        if current[0] == init[0] and current[1] == init[1]:
            break

    return path


path = search(grid, init, goal, cost)

for row in path:
    print(row)

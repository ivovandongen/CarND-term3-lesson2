# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
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


def mark_expansion(count, grid, move):
    grid[move[0]][move[1]] = count


def possible_moves(grid, position):
    moves = []
    for move in delta:
        next_pos = [position[0] + move[0], position[1] + move[1]]
        if min(next_pos) >= 0 \
                and next_pos[0] < len(grid) \
                and next_pos[1] < len(grid[1]) \
                and grid[next_pos[0]][next_pos[1]] is 0:
            moves.append(next_pos)

    return moves


def search(grid, init, goal, cost, heuristic):

    # Little helper to keep things readable
    f = lambda g, point : g + heuristic[point[0]][point[1]]

    open_list = [[f(0, init), 0] + init]
    expansion = 0
    expansions = [[-1 for x in range(len(grid[0]))] for x in range(len(grid))]
    while len(open_list) > 0:
        # Take element with lowest F value
        current_pos = min(open_list, key=lambda x: x[0])

        # Mark expansion
        mark_expansion(expansion, expansions, current_pos[2:4])
        expansion += 1

        # Check if we're done
        if current_pos[2] is goal[0] and current_pos[3] is goal[1]:
            return expansions

        # Find possible moves
        moves = possible_moves(grid, current_pos[2:4])

        # Set new F and G value
        moves = [[f(current_pos[1] + cost, x), current_pos[1] + cost] + x for x in moves]

        # check last move off and append new moves
        open_list += [x for x in moves if x not in open_list]
        open_list.remove(current_pos)
        mark_used(grid, current_pos[2:4])

    return 'fail'


exp = search(grid, init, goal, cost, heuristic)
for row in exp:
    print(row)

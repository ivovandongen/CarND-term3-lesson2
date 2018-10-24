# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def mark_used(grid, move):
    grid[move[0]][move[1]] = 1


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


def compute_value(grid, goal, cost):
    values = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    current_cost = 0
    open_list = [[current_cost] + goal]
    while len(open_list) > 0:
        current_cost += cost
        moves = []
        for pos in open_list:
            values[pos[1]][pos[2]] = pos[0]
            mark_used(grid, pos[1:3])
            moves += possible_moves(grid, pos[1:3])
        open_list = [[current_cost] + x for x in moves if x not in open_list]

    return values


values = compute_value(grid, goal, cost)

for row in values:
    print([str(item).zfill(2) for item in row])

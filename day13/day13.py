from typing import Tuple


def get_input():
    grid = []

    def get_above():
        return grid[-1][len(row)][1][0]

    def get_left():
        return row[-1][1][0]

    with open('input-example.txt', 'r') as f:
        track = 0
        for line in f:
            row = []
            for c in line.rstrip('\n'):
                grid_ids = []
                if c == '/':
                    # Bottom right
                    if row and row[-1][0] in '-+':
                        grid_ids.append(get_left())
                    else:
                        # Top left (new track)
                        grid_ids.append(track)
                        track += 1
                    pass
                elif c == '\\':
                    # Top right
                    if row and row[-1][0] in '-+':
                        grid_ids.append(get_left())
                    else:
                        # Bottom left
                        grid_ids.append(0)
                elif c == '-':
                    grid_ids.append(get_left())
                elif c == '|':
                    # Get track id of row above
                    grid_ids.append(get_above())
                    pass
                elif c == '+':
                    # Get track id of left and above
                    grid_ids.append(get_left())
                    grid_ids.append(get_above())
                elif c in '<>':
                    grid_ids.append(get_left())
                elif c in '^v':
                    grid_ids.append(get_above())
                row.append((c, grid_ids))

            grid.append(row)

    return grid


def turn_curve(c_dir, point):
    if point == '/':
        return 1 if c_dir in '^v' else -1
    elif point == '\\':
        return -1 if c_dir in '^v' else 1


def turn(c_dir, c_turn):
    types = '^<v>'
    return types[types.index(c_dir) + c_turn]


grid = get_input()
carts = []

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col][0] in 'v^<>':
            carts.append([grid[row][col][0], (row, col), -1])
print(carts)

crash = None
while not crash:
    for cart in carts:
        cart_dir = cart[0]
        cart_pos: Tuple[int, int] = cart[1]
        cart_turn = cart[2]
        new_pos = None

        if cart_dir == '>':
            new_pos = grid[cart_pos[0]][cart_pos[1] + 1]
        elif cart_dir == '<':
            new_pos = grid[cart_pos[0]][cart_pos[1] - 1]
        elif cart_dir == '^':
            new_pos = grid[cart_pos[0] - 1][cart_pos[1]]
        elif cart_dir == 'v':
            new_pos = grid[cart_pos[0] + 1][cart_pos[1]]

        if new_pos[0] == '+':
            new_dir = turn(cart_dir, cart_turn)
        elif new_pos[0] in '\\/':
            new_dir = turn(cart_dir, turn_curve(cart_dir, new_pos))
        elif new_pos[0] == '-':

        print("CRASH")

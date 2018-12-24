def get_input():
    grid = []
    carts = {}
    cart_id = 0

    with open('input-example.txt', 'r') as f:
        y = 0
        for line in f:
            row, x = [], 0
            for c in line.rstrip('\n'):
                if c in '<>':
                    row.append('-')
                    carts[cart_id] = ([c, [x, y], -1])
                    cart_id += 1
                elif c in '^v':
                    row.append('|')
                    carts[cart_id] = ([c, [x, y], -1])
                    cart_id += 1
                else:
                    row.append(c)
                x += 1

            grid.append(row)
            y += 1

    return grid, carts


def turn_curve(c_dir, point):
    if point == '/':
        return 1 if c_dir in '^v' else -1
    elif point == '\\':
        return -1 if c_dir in '^v' else 1


def turn(c_dir, c_turn):
    types = '^>v<'
    return types[(types.index(c_dir) + c_turn) % len(types)]


grid, carts = get_input()

crash = None

positions = {}
positions_inv = {}

while not crash:

    sorted_carts = sorted(carts.items(), key=lambda c: (c[1][1][1], c[1][1][0]))
    for cart in sorted_carts:
        cart_id = cart[0]
        cart_dir = cart[1][0]
        cart_pos = cart[1][1]
        cart_turn = cart[1][2]

        if cart_id not in carts.keys():
            continue

        positions_inv.setdefault((cart_pos[0], cart_pos[1]), set()).discard(cart_id)

        if cart_dir == '>':
            cart_pos[0] += 1
        elif cart_dir == '<':
            cart_pos[0] -= 1
        elif cart_dir == '^':
            cart_pos[1] -= 1
        elif cart_dir == 'v':
            cart_pos[1] += 1

        grid_val = grid[cart_pos[1]][cart_pos[0]]

        if grid_val == '+':
            cart[1][0] = turn(cart_dir, cart_turn)
            cart[1][2] = (cart_turn + 2) % 3 - 1
        elif grid_val in '\\/':
            cart[1][0] = turn(cart_dir, turn_curve(cart_dir, grid_val))

        inv = positions_inv.setdefault((cart_pos[0], cart_pos[1]), set())
        inv.add(cart_id)

        positions[cart_id] = (cart_pos[0], cart_pos[1])

        if len(inv) == 2:
            for cid in inv:
                carts.pop(cid)
                positions.pop(cid)






    if len(carts) == 1:
        print(carts)
        break

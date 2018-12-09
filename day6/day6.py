coords = []
max_x = 0
max_y = 0
with open('input.txt', 'r') as f:
    for line in f:
        coord = tuple(int(l.strip()) for l in line.split(','))
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
        coords.append(coord)

coords = sorted(coords)

coords = [(i, coords[i]) for i in range(len(coords))]

print(coords)

stack = []

grid = {}

print(grid)
while len(stack) > 0:

    new_stack = []

    for guy in stack:
        guy_id, coords = guy[0], guy[1]

        if grid.get(coords) is not None:



    stack = new_stack



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

sorted_coords = sorted(coords)

coords = [(i, sorted_coords[i]) for i in range(len(coords))]

stack = coords

grid = [[-1 for j in range(max_y + 1)] for i in range(max_x + 1)]

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
while len(stack) > 0:

    new_stack = []

    candidates = {}

    for guy in stack:
        guy_id, coords = guy[0], guy[1]

        if grid[coords[0]][coords[1]] == -1:
            candidates.setdefault(coords, set()).add(guy_id)

    for k, v in candidates.items():
        key = next(iter(v)) if len(v) == 1 else '.'

        grid[k[0]][k[1]] = key

        for move in moves:
            x, y = k[0] + move[0], k[1] + move[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                new_stack.append((key, (x, y)))

    stack = new_stack

counts = {}

infinites = set()

for i in range(max_x):
    infinites.add(grid[i][0])
    infinites.add(grid[i][-1])
for i in range(max_y):
    infinites.add(grid[0][i])
    infinites.add(grid[-1][i])

for row in grid:
    for guy in row:
        if guy not in infinites:
            counts[guy] = counts.setdefault(guy, 0) + 1

print(sorted(counts.values(), reverse=True)[0])


# Part 2

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


grid = [[-1 for j in range(max_y + 1)] for i in range(max_x + 1)]
count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        dis = sum([distance((i, j), coord) for coord in sorted_coords])
        if dis < 10000:
            count += 1

print(count)

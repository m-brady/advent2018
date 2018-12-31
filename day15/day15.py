import heapq

area = []

goblins = []
elves = []


def get_targets(pos):
    return goblins if pos in elves else elves


def adjacent(square):
    x, y = square[0], square[1]
    adj = []

    if x > 0:
        adj.append((x - 1, y))
    if x < len(area[y]) - 1:
        adj.append((x + 1, y))
    if y > 0:
        adj.append((x, y - 1))
    if y < len(area) - 1:
        adj.append((x, y + 1))

    return adj


def in_range(squares, cur):
    return [sq for sq in squares if area[sq[1]][sq[0]] != '#' or sq == cur]


def attack(squares, cur):
    pass


def move(start, squares_in_range):
    seen = {start}

    heap = [((0, start[1], start[0]), start)]
    heapq.heapify(heap)

    nearest = []
    while heap:
        guy = heapq.heappop(heap)
        depth = guy[0][0]

        adj = adjacent(guy[1])
        print(adj)
        we_there = [(depth, a[1], a[0]) for a in adj if a in squares_in_range]
        print(we_there)
        if we_there:
            nearest += we_there
        else:
            good_adj = in_range(adj, guy[1])
            for ga in good_adj:
                if ga not in seen:
                    heapq.heappush(heap, ((depth + 1, ga[1], ga[0]), ga))

    return nearest


with open('input-test.txt', 'r') as f:
    y = 0
    for line in f:
        row, x = [], 0
        for c in line.rstrip():
            row.append(c)

            if c == 'G':
                goblins.append((x, y))
            if c == 'E':
                elves.append((x, y))

            x += 1
        y += 1

        area.append(row)

pos = (1, 1)
targets = get_targets(pos)
print(targets)
squares_in_range = [adjacent(sq) for sq in targets]
squares_in_range = {sq for sublist in squares_in_range for sq in sublist}

print(squares_in_range)
print("------------------------------------------------")

to_move = move(pos, squares_in_range)
print("move",to_move)

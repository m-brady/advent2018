area = []

goblins = []
elves = []


def adjacent(square):
    x, y = square[0], square[1]
    adj = []

    if x > 0 and area[y][x - 1] == '.':
        adj.append((x - 1, y))
    if x < len(area[y]) - 1 and area[y][x + 1] == '.':
        adj.append((x + 1, y))
    if y > 0 and area[y - 1][x] == '.':
        adj.append((x, y - 1))
    if y < len(area) - 1 and area[y + 1][x] == '.':
        adj.append((x, y + 1))

    return adj


def walk(start, targets):
    seen = set()

    def walk(square):
        seen.add(square)
        adj = [s for s in adjacent(square) if s not in seen]

def get_in_range(targets):



with open('input.txt', 'r') as f:
    x = 0
    for line in f:
        row, y = [], 0
        for c in line.rstrip():
            row.append(c)

            if c == 'G':
                goblins.append((x, y))
            if c == 'E':
                elves.append((x, y))

        area.append(row)

for row in area:
    print(row)

combat_round = 0

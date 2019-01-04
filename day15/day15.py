import functools
import heapq
from dataclasses import dataclass

area = []
units = []


@dataclass
class Unit:
    race: str
    attack: int = 3
    health: int = 200


def get_targets(unit):
    return [u for u in units if u[2].race != unit.race]


def adjacent(pos):
    y, x = pos[0], pos[1]
    adj = []

    if y > 0:
        adj.append((y - 1, x))
    if x > 0:
        adj.append((y, x - 1))
    if x < len(area[y]) - 1:
        adj.append((y, x + 1))
    if y < len(area) - 1:
        adj.append((y + 1, x))
    return adj


def walkable(squares):
    return [sq for sq in squares if area[sq[0]][sq[1]] == '.']


def in_range(squares, cur):
    return [sq for sq in squares if area[sq[0]][sq[1]] == '.' or sq == cur]


def attack(pos, targets):
    adj_squares = set(adjacent(pos))
    adj_targets = [target for target in targets if target[1] in adj_squares]

    return next(iter(sorted(adj_targets, key=lambda target: (target[2].health, target[1]))))


def walk2(start, targets):

    seen = {}
    heap = [(0, [start])]
    heapq.heapify(heap)

    paths = []

    while heap:
        guy = heapq.heappop(heap)
        depth, path, cur = guy[0], guy[1], guy[1][-1]

        best_depth = seen.get(cur)
        if not best_depth or depth < best_depth:
            seen[cur] = depth

            if cur in targets:
                paths.append((depth, path))
            else:
                adjs = walkable(adjacent(cur))
                for adj in adjs:
                    heapq.heappush(heap, (depth + 1, path + [adj]))

    return min(paths)[1][1] if paths else None





def walk(start, squares_in_range):
    seen = {start: 0}

    if start in squares_in_range:
        return None

    heap = [((0, start[0], start[1]), [start])]

    moves = set()
    while heap:
        guy = heapq.heappop(heap)
        depth = guy[0][0]
        path = guy[1]
        cur = path[-1]

        if cur in squares_in_range:
            moves.add((depth, path[1]))
        else:
            adj = walkable(adjacent(cur))
            for sq in adj:
                if sq not in seen.keys() or seen[sq] > depth:
                    heapq.heappush(heap, ((depth + 1, sq[0], sq[1]), path + [sq]))
                    seen[sq] = depth

    return min(moves)[1] if moves else None


def solve():
    while units:
        turn, pos, unit = units[0][0], units[0][1], units[0][2]
        # print(units)
        # print(turn, pos, unit)
        targets = get_targets(unit)

        if not targets:
            break

        target_ranges = set()
        for target in targets:
            target_ranges.update(in_range(adjacent(target[1]), pos))

        if pos not in target_ranges:
            next_pos = walk2(pos, target_ranges)
            if next_pos:
                area[pos[0]][pos[1]], area[next_pos[0]][next_pos[1]] = '.', unit.race
                pos = next_pos

        if pos in target_ranges:
            target = attack(pos, targets)
            target[2].health -= unit.attack

            if target[2].health <= 0:
                units.remove(target)
                area[target[1][0]][target[1][1]] = '.'

        heapq.heapreplace(units, (turn + 1, pos, unit))


with open('input.txt', 'r') as f:
    y = 0
    for line in f:
        row, x = [], 0
        for c in line.rstrip():
            row.append(c)

            if c == 'G':
                heapq.heappush(units, (0, (y, x), Unit(race='G')))
            if c == 'E':
                heapq.heappush(units, (0, (y, x), Unit(race='E')))

            x += 1
        y += 1

        area.append(row)

# pos = (1, 1)
# targets = get_targets(pos)
# print(targets)
# squares_in_range = [adjacent(sq) for sq in targets]
# squares_in_range = {sq for sublist in squares_in_range for sq in sublist}
#
# print(squares_in_range)
# print("------------------------------------------------")
#
# to_move = move(pos, squares_in_range)
# print("move", to_move)

solve()
rounds = min(units, key=lambda unit: unit[0])[0]
print(min(units, key=lambda unit: unit[0]))

print(units)

health_sum = functools.reduce(lambda a, unit: a + unit[2].health, units, 0)
print(health_sum)
print(rounds * health_sum)

import re

PATTERN = 'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>'

og_guys = []

with open('input.txt', 'r') as f:
    for line in f:
        match = re.findall(PATTERN, line)[0]
        x, y = int(match[0]), int(match[1])
        dx, dy = int(match[2]), int(match[3])
        og_guys.append(([x, y], (dx, dy)))

guys = og_guys.copy()

for second in range(1, 50000):
    x_min, x_max = 1e10, 0
    y_min, y_max = 1e10, 0
    for guy in guys:
        guy[0][0] = guy[0][0] + guy[1][0]
        guy[0][1] = guy[0][1] + guy[1][1]

        x_min = min(guy[0][0], x_min)
        x_max = max(guy[0][0], x_max)
        y_min = min(guy[0][1], y_min)
        y_max = max(guy[0][1], y_max)

    # print(second, y_max, y_min, x_max, x_min)
    if y_max - y_min == 9:
        break

print(second)
# 21388
grid = [['.' for i in range(62)] for j in range(10)]
for guy in guys:
    grid[guy[0][1] - y_min][guy[0][0] - x_min] = '#'

for row in grid:
    print(row)

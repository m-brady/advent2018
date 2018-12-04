import re

PATTERN = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

coords = {}
ids = set()
with open('input.txt', 'r') as f:
    for line in f:
        match = re.findall(PATTERN, line.rstrip())[0]
        cid = int(match[0])
        left, top = int(match[1]), int(match[2])
        right, bottom = left + int(match[3]), top + int(match[4])
        ids.add(cid)
        for i in range(left, right):
            for j in range(top, bottom):
                coords[(i, j)] = coords.setdefault((i, j), []) + [cid]

summ = 0

for k, v in coords.items():
    if len(v) > 1:
        summ += 1
    if len(v) > 1:
        for guy in v:
            if guy in ids:
                ids.remove(guy)

# Part 1
print(summ)
# Part 2
print(ids)

import re

PATTERN = '\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (?:Guard #(\d+) )?(begins shift|wakes up|falls asleep)'

records = []

with open('input.txt', 'r') as f:
    for line in f:
        match = re.findall(PATTERN, line.rstrip())[0]

        date = (int(match[0]), int(match[1]), int(match[2]), int(match[3]), int(match[4]))
        action = match[5]
        gid = match[6]

        records.append((date, action, gid))

records = sorted(records, key=lambda r: r[0])

naps = {}
cur_guard = 0
start = 0
for record in records:
    if record[1]:
        cur_guard = record[1]
    elif record[2] == 'falls asleep':
        start = record[0][4]
    elif record[2] == 'wakes up':
        for i in range(start, record[0][4]):
            guard_naps = naps.setdefault(cur_guard, [0] * 60)
            guard_naps[i] += 1

# Part 1
sleepy_guard, time = 0, 0
for guard, guard_naps in naps.items():
    if sum(guard_naps) > time:
        sleepy_guard, time = guard, sum(guard_naps)

hour = naps[sleepy_guard].index(max(naps[sleepy_guard]))
print(int(sleepy_guard) * hour)

# Part 2
sleepy_guard, maxtime = 0, 0

for guard, guard_naps in naps.items():
    if max(guard_naps) > maxtime:
        sleepy_guard, maxtime = guard, max(guard_naps)

print(int(sleepy_guard) * naps[sleepy_guard].index(maxtime))

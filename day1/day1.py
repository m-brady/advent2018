# PART 1

with open('input.txt', 'r') as f:
    freq = 0
    for line in f:
        change = int(line)
        freq += change

print(freq)

# PART 2

changes = []
with open('input.txt', 'r') as f:
    freq = 0
    for line in f:
        changes.append(int(line))

freq = changes[0]
seen = set()
idx = 1

while freq not in seen:
    seen.add(freq)
    freq += changes[idx]

    idx += 1
    if idx == len(changes):
        idx = 0

print(freq)

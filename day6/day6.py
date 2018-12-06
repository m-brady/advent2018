coords = []

with open('input.txt', 'r') as f:
    for line in f:
        coords.append(tuple(int(l.strip()) for l in line.split(',')))

print(coords)

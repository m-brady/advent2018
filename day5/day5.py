import string

line = ''

with open('input.txt', 'r') as f:
    line = f.readline().rstrip()

idx = 1
chars = [line[0]]

while idx < len(line):
    cur = line[idx]
    if len(chars) > 0 and abs(ord(chars[-1]) - ord(cur)) == 32:
        chars.pop()
    else:
        chars.append(cur)

    idx = idx + 1

print(len(chars))

# Part 2
size = -1

for i in range(0, 26):
    pruned = line.replace(string.ascii_lowercase[i], '')
    pruned = pruned.replace(string.ascii_uppercase[i], '')

    idx = 1
    chars = [pruned[0]]

    while idx < len(pruned):
        cur = pruned[idx]
        if len(chars) > 0 and abs(ord(chars[-1]) - ord(cur)) == 32:
            chars.pop()
        else:
            chars.append(cur)

        idx = idx + 1

    if size == -1 or len(chars) < size:
        size = len(chars)
print(size)

c

twos = 0
threes = 0

for box in lines:
    freq = {}
    for char in box:
        val = freq.setdefault(char, 0)
        freq[char] = val + 1

    has_two = 0
    has_three = 0
    for k, v in freq.items():
        if v == 2:
            has_two = 1
        elif v == 3:
            has_three = 1
    twos += has_two
    threes += has_three

print(twos * threes)

# PART 2
with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

    for i in range(0, len(lines)):
        for j in range(i + 1, len(lines)):

            diffs = 0
            diff = -1
            for idx, (a, b) in enumerate(zip(lines[i], lines[j])):
                if a != b:
                    diffs += 1
                    diff = idx

            if diffs == 1:
                guy = lines[i][:diff] + lines[i][diff + 1:]
                print(guy)

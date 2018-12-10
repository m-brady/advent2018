import heapq
import re
import string

pattern = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."

required_by = {char: set() for char in list(string.ascii_uppercase)}
requires = {char: set() for char in list(string.ascii_uppercase)}

stack = list(string.ascii_uppercase)

with open('input.txt', 'r') as f:
    for line in f:
        match = re.findall(pattern, line)[0]
        required_by[match[0]].add(match[1])
        requires[match[1]].add(match[0])

order = ''
seen = set()
done = set()
while len(stack) > 0:

    guy = next(guy for guy in stack if done.issuperset(requires[guy]))

    stack.remove(guy)
    done.add(guy)
    order += guy
    for g in required_by[guy]:
        if g not in seen:
            seen.add(g)

print(order)

# Part 2
progress = []
done = set()
stack = list(string.ascii_uppercase)


def get_time(char):
    return 61 + ord(char) - ord('A')


second = 0
while len(stack) > 0:
    while len(progress) > 0 and heapq.nsmallest(1, progress)[0][0] == second:
        guy = heapq.heappop(progress)
        done.add(guy[1])

    guys = (guy for guy in stack if done.issuperset(requires[guy]))
    guy = next(guys, None)
    while len(progress) < 5 and guy is not None:
        heapq.heappush(progress, (second + get_time(guy), guy))
        stack.remove(guy)
        guy = next(guys, None)

    second = heapq.nsmallest(1, progress)[0][0]

print(second)

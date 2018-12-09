import heapq
import re
import string

pattern = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."

fsm = {char: set() for char in list(string.ascii_uppercase)}
inv_fsm = {char: set() for char in list(string.ascii_uppercase)}

stack = list(string.ascii_uppercase)

with open('input.txt', 'r') as f:
    for line in f:
        match = re.findall(pattern, line)[0]
        fsm[match[0]].add(match[1])
        inv_fsm[match[1]].add(match[0])

order = ''
seen = set()
done = set()
while len(stack) > 0:

    guy = next(guy for guy in stack if done.issuperset(inv_fsm[guy]))

    stack.remove(guy)
    done.add(guy)
    order += guy
    print(fsm[guy])
    for g in fsm[guy]:
        if g not in seen:
            seen.add(g)
    print(guy)


print(order)
import itertools
import re


def get_input():
    state_pattern = 'initial state: ([#\.]+)'
    pattern = '([#\.]{5}) => ([#.])'

    with open('input.txt', 'r') as f:
        initial_state = re.findall(state_pattern, f.readline())[0]
        f.readline()
        state_changes = dict([re.findall(pattern, line.rstrip())[0] for line in f])
        return initial_state, state_changes


def pad_left(state: str, n):
    size = sum(1 for _ in itertools.takewhile(lambda pot: pot == '.', itertools.islice(state, n)))
    return ((n - size - 1) * '.') + state


def pad_right(state: str, n):
    size = sum(1 for _ in itertools.takewhile(lambda pot: pot == '.', itertools.islice(reversed(state), n)))
    return state + ((n - size - 1) * '.')


def go(initial_state, state_changes, num_generations):
    state = initial_state
    print(state)
    zero = 0
    for generation in range(num_generations):
        # Ensure that there are some '.'s to the left and right of the current state
        zero -= len(state)
        state = pad_left(state, 5)
        zero += len(state)
        state = pad_right(state, 5)

        new_state = state

        for i in range(2, len(state) - 2):
            section = state[i - 2: i + 3]
            change = state_changes.get(section)

            if change:
                new_state = new_state[:i] + change + new_state[i + 1:]
            else:
                new_state = new_state[:i] + '.' + new_state[i + 1:]

        state = new_state
        guys = list(filter(lambda a: a[1] == '#', enumerate(state, -zero)))
        start = guys[0]
        length = len(guys)
        guys = map(lambda a: a[0] - start[0], guys)
        partial = sum(guys)
        # print(generation, start[0], generation-start[0], list(guys), partial, length)

        guess = (length * start[0]) + partial
        # print(length, start[0], partial)
        # print(generation, guess, partial)
        # print(generation, sum(map(lambda a: a[0], filter(lambda a: a[1] == '#', enumerate(state, -zero)))))

    # print(state)
    # print(list(enumerate(state, -zero)))
    #
    # print(list(filter(lambda a: a[1] == '#', enumerate(state, -zero))))
    # print(list(map(lambda a: a[0], filter(lambda a: a[1] == '#', enumerate(state, -zero)))))

    # print(sum(map(lambda a: a[0], filter(lambda a: a[1] == '#', enumerate(state, -zero)))))
    return zero, state


input = get_input()
print(input)

zero, state = go(input[0], input[1], 2000)
result = filter(lambda a: a[1] == '#', enumerate(state, -zero))
start = list(result)[0]
print(start)
result = map(lambda a: a[0]- start[0], filter(lambda a: a[1] == '#', enumerate(state, -zero)))
print((49999999920*42) + sum(result))
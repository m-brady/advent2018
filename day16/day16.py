import re

PATTERN = r'(\d,? \d,? \d,? \d)'

with open('input.txt', 'r') as f:
    samples = []

    sample = []

    for line in f:

        if line.isspace():
            samples.append(sample)
            sample = []
        else:
            match = re.findall(PATTERN, line.rstrip())
            values = re.split(r',?\W+', match[0])
            sample.append([int(val) for val in values])

opt_codes = {'addr': lambda register, a, b: register[a] + register[b],
             'addi': lambda register, a, b: register[a] + b,
             'mulr': lambda register, a, b: register[a] * register[b],
             'muli': lambda register, a, b: register[a] * b,
             'banr': lambda register, a, b: register[a] & register[b],
             'bani': lambda register, a, b: register[a] & b,
             'borr': lambda register, a, b: register[a] | register[b],
             'bori': lambda register, a, b: register[a] | b,
             'setr': lambda register, a, b: register[a],
             'seti': lambda register, a, b: a,
             'gtir': lambda register, a, b: a > register[b],
             'gtri': lambda register, a, b: register[a] > b,
             'gtrr': lambda register, a, b: register[a] > register[b],
             'eqir': lambda register, a, b: a == register[b],
             'eqri': lambda register, a, b: register[a] == b,
             'eqrr': lambda register, a, b: register[a] == register[b]}

mapping = {}
instruction_mappings = {}

three_plus = 0

for sample in samples:
    registers, instruction, result = sample[0], sample[1], sample[2]

    matches = set()
    for opt_code in opt_codes:
        val = opt_codes[opt_code](registers, instruction[1], instruction[2])
        if result[3] == val:
            matches.add(opt_code)

    if matches >= 3:
        three_plus += 1
    existing_matches = mapping.get(instruction[0])
    if not existing_matches:
        mapping[instruction[0]] = matches
    else:
        mapping[instruction[0]].intersection(matches)

print(len([m for m in mapping.values() if len(m) >= 3]))

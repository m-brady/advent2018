import re

PATTERN = r'(\d+,? \d,? \d,? \d)'

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

op_codes = {'addr': lambda register, a, b: register[a] + register[b],
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

three_plus = 0

op_code_mapping = {}

for sample in samples:
    registers, result = sample[0], sample[2]
    op_code_num, a, b, c = sample[1][0], sample[1][1], sample[1][2], sample[1][3]
    matches = set()
    for op_code in op_codes:
        val = op_codes[op_code](registers, a, b)
        if result[c] == val:
            matches.add(op_code)

    for match in matches:
        op_code_mapping.setdefault(match, set()).add(op_code_num)

    if len(matches) >= 3:
        three_plus += 1

print(three_plus)

seen = set()

while len(seen) < 15:
    removed = False
    for op_code_name, op_code_nums in op_code_mapping.items():
        if len(op_code_nums) == 1:
            guy = next(iter(op_code_nums))
            if guy not in seen:
                seen.add(guy)
                for name, nums in op_code_mapping.items():
                    if name != op_code_name:
                        nums.difference_update(op_code_nums)

print(op_code_mapping)

id_to_fn = {}
for k, v in op_code_mapping.items():
    id_to_fn[next(iter(v))] = op_codes[k]

pattern = r'\d+ \d+ \d+ \d+'
instructions = []
with open('input2.txt', 'r') as f:
    for line in f:
        match = re.split(r'\W+', line.rstrip())
        instructions.append(tuple(int(d) for d in match))

registers = [0, 0, 0, 0]
for instruction in instructions:
    fn = id_to_fn[instruction[0]]
    val = fn(registers,instruction[1],instruction[2])
    registers[instruction[3]] = val

print(registers)
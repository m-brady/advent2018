input = 323081

input_list = [3, 2, 3, 0, 8, 1]

elf_0 = 0
elf_1 = 1

guys = [3, 7]

while len(guys) < input + 10:
    new_recipe = guys[elf_0] + guys[elf_1]
    if new_recipe > 9:
        guys.append(new_recipe // 10)
    guys.append(new_recipe % 10)

    elf_0 = (elf_0 + 1 + guys[elf_0]) % len(guys)
    elf_1 = (elf_1 + 1 + guys[elf_1]) % len(guys)

print(''.join(str(i) for i in guys[input:input + 10]))

elf_0 = 0
elf_1 = 1

guys = [3, 7]

not_found = True
answer = None
while not answer:
    new_recipe = guys[elf_0] + guys[elf_1]
    if new_recipe > 9:
        guys.append(new_recipe // 10)
        if guys[-len(input_list):] == input_list:
            answer = len(guys) - len(input_list)
            break

    guys.append(new_recipe % 10)
    if guys[-len(input_list):] == input_list:
        answer = len(guys) - len(input_list)
        break

    elf_0 = (elf_0 + 1 + guys[elf_0]) % len(guys)
    elf_1 = (elf_1 + 1 + guys[elf_1]) % len(guys)


print(answer)

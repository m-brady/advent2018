with open('input.txt', 'r') as f:
    line = f.readline()
    guys = [int(guy) for guy in line.split()]
    print(guys)


def fun(guys):
    child_nodes, meta_entries = guys.pop(0), guys.pop(0)

    meta_sum = 0
    for i in range(child_nodes):
        meta_sum += fun(guys)

    for meta in range(meta_entries):
        meta_sum += guys.pop(0)

    return meta_sum


result = fun(guys.copy())
print(result)


# Part 2

def fun(guys):
    child_nodes, meta_entries = guys.pop(0), guys.pop(0)

    meta_sum = 0
    meta_dict = {}
    for i in range(child_nodes):
        meta_dict[i] = fun(guys)

    for idx in range(meta_entries):
        meta = guys.pop(0)
        if child_nodes == 0:
            meta_sum += meta
        else:
            meta_sum += meta_dict.get(meta - 1, 0)

    return meta_sum


result = fun(guys)
print(result)

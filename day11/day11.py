serial = 39
size = 300

grid = [[0 for j in range(size)] for i in range(size)]

for x in range(size):
    rack_id = (x + 1) + 10
    for y in range(size):
        power_level = rack_id * (y + 1)
        power_level += serial
        power_level *= rack_id

        power_level = (power_level % 1000) // 100
        power_level -= 5

        grid[y][x] = power_level

top_left = (0, 0)
max_sum = 0


cur_sum = 0

print(grid)

for j in range(3):
    for i in range(3):
        cur_sum += grid[j][i]

print(cur_sum)

col_sums = []
for i in range(size):
    col_sums.append(grid[0][i] + grid[1][i] + grid[2][i])
print(col_sums)

square_sums = [[col_sums[0] + col_sums[1] + col_sums[2]]]
for i in range(1,size - 2):
    square_sums[0].append(square_sums[0][i-1] - col_sums[i-1] + col_sums[i+2])

print(square_sums)

# for x in range(1,size-2):
#     old_col = grid[0][x-1] + grid[1][x-1] + grid[2][x-1]
#     new_col = grid[0][x+2] + grid[1][x+2] + grid[2][x+2]
#     col_sums.append(col_sums[x-1] - old_col + new_col)
#
# print(col_sums)






y = 0
for x in range(size-2):
    left_col_sum = grid[y][x-1] + grid[y+1][x-1] + grid[y+2][x-1]
    right_col_sum = grid[y][x+2] + grid[y+1][x+2] + grid[y+2][x+2]





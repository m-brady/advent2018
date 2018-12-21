
def go(serial, size, square_size):

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

    col_sums = [sum(grid[j][i] for j in range(square_size)) for i in range(size)]

    square_sums = [[]]
    cur_sum = col_sums[0] + col_sums[1]
    for i in range(0, size - 2):
        prev_col = 0 if i == 0 else col_sums[i - 1]
        cur_sum = cur_sum - prev_col + col_sums[i + 2]
        square_sums[0].append(cur_sum)

    row_sums = []
    for row in range(size):
        row_sum, cur_sum = [], grid[row][0] + grid[row][1]
        for col in range(size - 2):
            prev = 0 if col == 0 else grid[row][col - 1]
            cur_sum = cur_sum - prev + grid[row][col + 2]
            row_sum.append(cur_sum)
        row_sums.append(row_sum)

    for row in range(1, size - 2):
        row_squares = []
        for col in range(0, size - 2):
            prev_row = row_sums[row - 1][col]
            last_square = square_sums[row - 1][col]
            square_sum = last_square - prev_row + row_sums[row + 2][col]
            row_squares.append(square_sum)
        square_sums.append(row_squares)

    max_guy, coords = -1, ()

    for y in range(len(square_sums)):
        for x in range(len(square_sums[y])):
            if square_sums[y][x] > max_guy:
                coords = (x,y)
                max_guy = square_sums[y][x]
    print(max_guy, coords)

go(3628, 300, 3)

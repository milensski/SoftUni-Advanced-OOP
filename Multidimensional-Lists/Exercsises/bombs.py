def get_childs(row, col, matrix):
    possible_childs = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),

        (row, col - 1),
        (row, col),
        (row, col + 1),

        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),

    ]

    children = []

    for child_row, child_col in possible_childs:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix):
            if matrix[child_row][child_col] > 0:
                children.append((child_row, child_col))

    return children


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]

    power = matrix[row][col]

    if power > 0:

        childs = get_childs(row, col, matrix)

        for child_row, child_col in childs:
            matrix[child_row][child_col] -= power

    else:
        continue

active_cell = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            active_cell.append(matrix[row][col])

print(f'Alive cells: {len(active_cell)}')
print(f'Sum: {sum(active_cell)}')
[print(' '.join(map(str, row))) for row in matrix]

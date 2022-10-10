def move(pos_row, pos_col, direction):
    pos_row += directions[direction][0]
    pos_col += directions[direction][1]

    return pos_row, pos_col


rows, cols = 6, 6

matrix = []

for _ in range(rows):
    matrix.append(input().split())

pos_row, pos_col = [int(x) for x in input().lstrip('(').rstrip(')').split(', ')]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:

    command = input().split(', ')

    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        direction, value = command[1], command[2]

        pos_row, pos_col = move(pos_row, pos_col, direction)

        if matrix[pos_row][pos_col] == '.':
            matrix[pos_row][pos_col] = value


    elif command[0] == 'Update':
        direction, value = command[1], command[2]
        pos_row, pos_col = move(pos_row, pos_col, direction)

        if matrix[pos_row][pos_col].isalnum():
            matrix[pos_row][pos_col] = value

    elif command[0] == 'Delete':

        direction = command[1]

        pos_row, pos_col = move(pos_row, pos_col, direction)

        if matrix[pos_row][pos_col].isalnum():
            matrix[pos_row][pos_col] = '.'

    elif command[0] == 'Read':
        direction = command[1]

        pos_row, pos_col = move(pos_row, pos_col, direction)

        if matrix[pos_row][pos_col].isalnum():
            print(matrix[pos_row][pos_col])

[print(*row, sep=' ') for row in matrix]

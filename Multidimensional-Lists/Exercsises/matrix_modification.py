size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])


def is_outside(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


while True:

    command = input()

    if command == 'END':
        break

    action, row, col, value = command.split()

    row = int(row)
    col = int(col)
    value = int(value)

    if action == 'Add':

        if is_outside(row,col,size):
            print('Invalid coordinates')
            continue

        matrix[row][col] += value

    elif action == 'Subtract':

        if is_outside(row,col,size):
            print('Invalid coordinates')
            continue

        matrix[row][col] -= value


for row in matrix:
    print(*row, sep=" ")


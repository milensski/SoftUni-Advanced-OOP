rows, cols = [int(x) for x in input().split()]

matrix = []


def out_of_range(row, col, rows, cols):
    if 0 <= row < rows and 0 <= col < cols:
        return False
    return True


for _ in range(rows):
    matrix.append(input().split())

while True:

    command = input().split()

    if command[0] == 'END':
        break

    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if out_of_range(row1, col1, rows, cols) or out_of_range(row2, col2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    [print(*row, sep=' ') for row in matrix]

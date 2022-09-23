import sys

rows, cols = [int(x) for x in input().split()]

matrix = []

max_size = -sys.maxsize

coordinates = (0, 0)

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        sum_of_submatrix = \
            sum([matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                 matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                 matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]])
        if sum_of_submatrix > max_size:
            coordinates = (row,col)
            max_size = sum_of_submatrix


row, col = coordinates
print(f'Sum = {max_size}')
for i in range(3):
    print(matrix[row+i][col], matrix[row+i][col + 1], matrix[row+i][col + 2])


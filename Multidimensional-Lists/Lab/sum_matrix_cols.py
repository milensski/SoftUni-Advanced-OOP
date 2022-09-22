rows, cols = [int(x) for x in input().split(', ')]

matrix = []


for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


for col in range(cols):
    sum_cols = 0
    for row in range(rows):
        sum_cols += matrix[row][col]
    print(sum_cols)
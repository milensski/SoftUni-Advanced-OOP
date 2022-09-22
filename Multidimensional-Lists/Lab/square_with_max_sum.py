rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

square_matrices = []

square_sum = {}

for row in range(rows - 1):
    for col in range(cols - 1):
       current_cell = matrix[row][col]
       right_cell = matrix[row][col+1]
       down_cell = matrix[row+1][col]
       down_right_cell = matrix[row+1][col+1]

       square_matrices.append((current_cell,right_cell,down_cell,down_right_cell))


for sub_matrix in square_matrices:
    if sum(sub_matrix) not in square_sum:
        square_sum[sum(sub_matrix)] = sub_matrix



result = max(square_sum.items())

sum_matrix = result[0]
sub_matrix = result[1]
row = 0
print(f'{sub_matrix[row]} {sub_matrix[row+1]}')
print(f'{sub_matrix[row+2]} {sub_matrix[row+3]}')

print(sum_matrix)
rows, cols = [int(x) for x in input().split(', ')]

matrix = []

sum_elements = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    sum_elements += sum(matrix[row])

print(sum_elements)
print(matrix)

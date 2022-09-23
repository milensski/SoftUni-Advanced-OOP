rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())


counter = 0

for row in range(rows-1):
    for col in range(cols-1):
        current_cell = matrix[row][col]
        left =  matrix[row][col+1]
        down = matrix[row+1][col]
        down_right = matrix[row+1][col+1]

        if current_cell == left == down == down_right:
            counter += 1

print(counter)

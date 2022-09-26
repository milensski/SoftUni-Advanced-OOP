def find_bunny(matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "B":
                return row, col


def right_path(start_row, start_col, matrix):
    sum_right = 0
    right_coordinates = []
    while start_col < size:
        if matrix[start_row][start_col] == 'X':
            break
        sum_right += (int(matrix[start_row][start_col]))
        right_coordinates.append([start_row,start_col])

        start_col += 1

    return 'right',sum_right,right_coordinates


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(input().split())

bunny_row, bunny_col = find_bunny(matrix)

best_score = 0

best_path = None

if right_path(bunny_row, bunny_col+1, matrix):
    sum_path, path_coordinates = right_path(bunny_row, bunny_col+1, matrix)

    if sum_path > best_score:
        best_score = sum_path
        best_path = path_coordinates
print(best_score)
print(best_path)
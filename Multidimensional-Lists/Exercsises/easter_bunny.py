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
            return False
        sum_right += (int(matrix[start_row][start_col]))
        right_coordinates.append([start_row,start_col])

    return sum_right,right_coordinates


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(input().split())

bunny_row, bunny_col = find_bunny(matrix)



if right_path(start_row, start_col+1, matrix):

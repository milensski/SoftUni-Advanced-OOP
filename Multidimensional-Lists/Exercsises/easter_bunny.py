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


def left_path(start_row, start_col, matrix):
    sum_left = 0
    left_coordinates = []
    while 0 <= start_col:
        if matrix[start_row][start_col] == 'X':
            break
        sum_left += (int(matrix[start_row][start_col]))
        left_coordinates.append([start_row,start_col])

        start_col -= 1

    return 'left',sum_left,left_coordinates

def up_path(start_row, start_col, matrix):
    sum_up = 0
    up_coordinates = []
    while 0 <= start_row:
        if matrix[start_row][start_col] == 'X':
            break
        sum_up += (int(matrix[start_row][start_col]))
        up_coordinates.append([start_row,start_col])

        start_row -= 1

    return 'up',sum_up,up_coordinates

def down_path(start_row, start_col, matrix):
    sum_down = 0
    down_coordinates = []
    while start_row < size:
        if matrix[start_row][start_col] == 'X':
            break
        sum_down += (int(matrix[start_row][start_col]))
        down_coordinates.append([start_row,start_col])

        start_row += 1

    return 'down',sum_down,down_coordinates


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(input().split())

bunny_row, bunny_col = find_bunny(matrix)

best_score = 0

best_path = None

best_direction = ''

if up_path(bunny_row-1, bunny_col, matrix):
    direction, sum_path, path_coordinates = up_path(bunny_row-1, bunny_col, matrix)

    if sum_path >= best_score:
        best_score = sum_path
        best_path = path_coordinates
        best_direction = direction

if down_path(bunny_row+1, bunny_col, matrix):
    direction, sum_path, path_coordinates = down_path(bunny_row+1, bunny_col, matrix)

    if sum_path >= best_score:
        best_score = sum_path
        best_path = path_coordinates
        best_direction = direction


if left_path(bunny_row, bunny_col-1, matrix):
    direction, sum_path, path_coordinates = left_path(bunny_row, bunny_col - 1, matrix)

    if sum_path >= best_score:
        best_score = sum_path
        best_path = path_coordinates
        best_direction = direction

if right_path(bunny_row, bunny_col + 1, matrix):
    direction,sum_path, path_coordinates = right_path(bunny_row, bunny_col+1, matrix)

    if sum_path >= best_score:
        best_score = sum_path
        best_path = path_coordinates
        best_direction = direction




print(best_direction)

print(*best_path, sep='\n')

print(best_score)
size = int(input())
race_number = input()

field = []
kilometers = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

tunnel_coordinates = []

for i in range(size):
    row_elements = input().split()
    field.append(row_elements)
    for j in range(size):
        if row_elements[j] == 'T':
            tunnel_coordinates.append([i, j])


row, col = 0, 0

while True:

    direction = input()

    if direction == "End":
        print(f'Racing car {race_number} DNF.')
        field[row][col] = 'C'
        break

    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if field[next_row][next_col] == '.':
        kilometers += 10
        row, col = next_row, next_col


    elif field[next_row][next_col] == 'T':
        field[next_row][next_col] = '.'
        kilometers += 30
        for tunel_row, tunel_col in tunnel_coordinates:
            if next_row == tunel_row and next_col == tunel_col:
                tunnel_coordinates.remove([tunel_row, tunel_col])

        row, col = tunnel_coordinates[0]
        field[row][col] = '.'

    elif field[next_row][next_col] == 'F':
        kilometers += 10
        print(f'Racing car {race_number} finished the stage!')
        field[next_row][next_col] = 'C'
        break

print(f'Distance covered {kilometers} km.')

[print(*row, sep='') for row in field]

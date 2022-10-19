def find_rover():
    for row in range(6):
        for col in range(6):
            if field[row][col] == 'E':
                return row, col


field = []

for _ in range(6):
    field.append(input().split())


commands = input().split(', ')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

rover_row, rover_col = find_rover()

deposits = {
    'W': [0,'Water'],
    'M': [0,'Metal'],
    'C': [0,'Concrete'],
}

for command in commands:

    move = directions[command]

    rover_row, rover_col = rover_row + move[0], rover_col + move[1]

    if rover_row >= 6:
        rover_row = 0
    elif rover_row < 0:
        rover_row = 5

    if rover_col >= 6:
        rover_col = 0
    elif rover_col < 0:
        rover_col = 5

    if field[rover_row][rover_col] in deposits:

        deposit = field[rover_row][rover_col]
        deposits[deposit][0] += 1
        name = deposits[deposit][1]

        print(f'{name} deposit found at ({rover_row}, {rover_col})')

    elif field[rover_row][rover_col] == 'R':

        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break


if deposits['W'][0] >= 1 and deposits['M'][0] >= 1 and deposits['C'][0] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

# for deposit in deposits.values():
#     if deposit[0] < 1:
#         print("Area not suitable to start the colony.")
#         break
# else:
#     print("Area suitable to start the colony.")


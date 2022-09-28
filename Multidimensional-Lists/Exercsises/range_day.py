def find_position(field, size):
    targets = []
    row = None
    col = None

    for r in range(size):
        for c in range(size):
            if field[r][c] == 'A':
                row = r
                col = c
            elif field[r][c] == 'x':
                targets.append([r, c])

    return row, col, targets


def shoot(direction, target_row, target_col, field):
    if direction == 'up':
        start_row = target_row - 1
        start_col = target_col
        while 0 <= start_row:
            if field[start_row][start_col] == 'x':
                field[start_row][start_col] = '.'
                total_targets.remove([start_row, start_col])
                hitted_targets.append([start_row, start_col])
                return 1
            start_row -= 1

    elif direction == 'down':
        start_row = target_row + 1
        start_col = target_col
        while start_row < size:
            if field[start_row][start_col] == 'x':
                field[start_row][start_col] = '.'
                total_targets.remove([start_row, start_col])
                hitted_targets.append([start_row, start_col])
                return 1
            start_row += 1

    elif direction == 'left':
        start_row = target_row
        start_col = target_col - 1
        while 0 <= start_col:
            if field[start_row][start_col] == 'x':
                field[start_row][start_col] = '.'
                total_targets.remove([start_row, start_col])
                hitted_targets.append([start_row, start_col])
                return 1

            start_col -= 1
    elif direction == 'right':
        start_row = target_row
        start_col = target_col - 1
        while start_col < size:
            if field[start_row][start_col] == 'x':
                field[start_row][start_col] = '.'
                total_targets.remove([start_row, start_col])
                hitted_targets.append([start_row, start_col])
                return 1
            start_col += 1

    return 0


def move(direction, value, target_row, target_col):
    if direction == 'up':
        while value > 0:
            if target_row - 1 >= 0:
                if field[target_row - 1][target_col] == '.':
                    field[target_row - 1][target_col] = 'A'
                    field[target_row][target_col] = '.'
                    value -= 1
                    target_row -= 1
            else:
                break
        return target_row, target_col

    elif direction == 'down':
        while value > 0:
            if target_row + 1 < size:
                if field[target_row - +1][target_col] == '.':
                    field[target_row - +1][target_col] = 'A'
                    field[target_row][target_col] = '.'
                    value -= 1
                    target_row += 1
            else:
                break
        return target_row, target_col

    elif direction == 'right':
        while value > 0:
            if target_col + 1 < size:
                if field[target_row][target_col + 1] == '.':
                    field[target_row][target_col + 1] = 'A'
                    field[target_row][target_col] = '.'
                    value -= 1
                    target_col += 1
            else:
                break
        return target_row, target_col

    elif direction == 'left':
        while value > 0:
            if target_col - 1 <= 0:
                if field[target_row][target_col - 1] == '.':
                    field[target_row][target_col - 1] = 'A'
                    field[target_row][target_col] = '.'
                    value -= 1
                    target_col -= 1
            else:
                break
        return target_row, target_col


size = 5

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}
field = []

for _ in range(size):
    field.append(input().split())

count_targets = 0

hitted_targets = []

n = int(input())

target_row, target_col, total_targets = find_position(field, size)

for _ in range(n):

    command = input().split()

    if command[0] == 'shoot':
        direction = command[1]
        count_targets += shoot(direction, target_row, target_col, field)


    elif command[0] == 'move':
        direction = command[1]
        value = int(command[2])

        target_row, target_col = move(direction, value, target_row, target_col)

    if len(total_targets) <= 0:
        print(f'Training completed! All {count_targets} targets hit.')
        break

if len(total_targets) > 0:
    print(f'Training not completed! {len(total_targets)} targets left.')

print(*hitted_targets, sep='\n')

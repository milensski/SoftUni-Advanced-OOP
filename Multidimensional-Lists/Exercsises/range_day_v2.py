
def get_next_pos(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    elif direction == 'down':
        return row + steps, col
    elif direction == 'left':
        return row, col - steps
    elif direction == 'right':
        return row,col + steps


def is_inrange(row,col,size):
    if 0 <= row < size and 0 <= col < size:
        return True

    return False


size = 5

matrix = []

player_row = 0
player_col = 0
targets = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'A':
            player_row = row
            player_col = col
        elif row_elements[col] == 'x':
            targets += 1
    matrix.append(row_elements)

n = int(input())

matrix[player_row][player_col] = '.'

hit_targets = []

for _ in range(n):

    command = input().split()

    action = command[0]
    direction = command[1]

    if action == 'move':
        steps = int(command[2])

        next_row, next_col = get_next_pos(player_row,player_col,direction,steps)

        if is_inrange(next_row,next_col,size):
            if matrix[next_row][next_col] == '.':
                player_row = next_row
                player_col = next_col

    else:

        bullet_row, bullet_col = get_next_pos(player_row,player_col,direction,1)

        while is_inrange(bullet_row,bullet_col,size):
            if matrix[bullet_row][bullet_col] == 'x':
                matrix[bullet_row][bullet_col] = '.'
                targets -= 1
                hit_targets.append([bullet_row,bullet_col])
                break
            bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, direction, 1)

    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print(*hit_targets, sep='\n')
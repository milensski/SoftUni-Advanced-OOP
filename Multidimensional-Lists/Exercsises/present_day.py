def get_next_pos(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    elif direction == 'down':
        return row + steps, col
    elif direction == 'left':
        return row, col - steps
    elif direction == 'right':
        return row, col + steps


def is_inrange(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True

    return False

def give_gifts(santa_row, santa_col, matrix):
    neighbours_coords = [
        [santa_row - 1,santa_col],
        [santa_row + 1,santa_col],
        [santa_row,santa_col - 1],
        [santa_row,santa_col + 1],

    ]

    gifts = 0
    nice = 0

    for r, c in neighbours_coords:
        if is_inrange(r, c, size):
            if matrix[r][c] == "V":
                gifts += 1
                nice += 1
            elif matrix[r][c] == "X":
                gifts += 1

            matrix[r][c] = '-'

    return gifts, nice


presents = int(input())
size = int(input())

santa_row = 0
santa_col = 0
nice_kids = 0
count_nice_kids = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row, santa_col = row, col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)




while presents > 0:

    direction = input()

    if direction == "Christmas morning":
        break

    next_row, next_col = get_next_pos(santa_row, santa_col, direction, 1)

    if is_inrange(next_row, next_col, size):

        if matrix[next_row][next_col] == 'X':
            matrix[santa_row][santa_col] = '-'
            matrix[next_row][next_col] = 'S'
            santa_row, santa_col = next_row, next_col

        elif matrix[next_row][next_col] == 'V':
            matrix[santa_row][santa_col] = '-'
            matrix[next_row][next_col] = 'S'
            presents -= 1
            nice_kids -= 1
            count_nice_kids += 1
            santa_row, santa_col = next_row, next_col

        elif matrix[next_row][next_col] == 'C':
            matrix[santa_row][santa_col] = '-'
            matrix[next_row][next_col] = 'S'
            santa_row, santa_col = next_row, next_col

            gifts, nice = give_gifts(santa_row, santa_col, matrix)

            presents -= gifts
            nice_kids -= nice
            count_nice_kids += nice
        else:
            matrix[santa_row][santa_col] = '-'
            matrix[next_row][next_col] = 'S'
            santa_row, santa_col = next_row, next_col

if presents <= 0 and nice_kids > 0:
    print(f'Santa ran out of presents!')

[print(*row) for row in matrix]

if nice_kids <= 0:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")


def position_of_objects(field):
    alice_row = None
    alice_col = None


    for row in range(size):
        for col in range(size):
            if field[row][col] == 'A':
                alice_row = row
                alice_col = col
            elif field[row][col] == 'R':
                hole_row = row
                hole_col = col

    return alice_row,alice_col


def in_range(row,col,size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())

field = []



for _ in range(size):
    field.append(input().split())



alice_row, alice_col = position_of_objects(field)


directions = {
    'up' : (-1,0),
    'down' : (1,0),
    'right' : (0,1),
    'left' : (0,-1),
    }

collected_tea = 0

while True:

    direction = input()

    field[alice_row][alice_col] = '*'

    move_row,move_col = directions[direction]

    new_row = move_row+alice_row
    new_col = move_col+alice_col

    if in_range(new_row,new_col,size):
        if field[new_row][new_col].isdigit():
            collected_tea += int(field[new_row][new_col])
            if collected_tea >= 10:
                field[new_row][new_col] = '*'
                print("She did it! She went to the party.")
                break
            else:
                field[new_row][new_col] = 'A'
                alice_row = new_row
                alice_col = new_col
        elif field[new_row][new_col] == 'R':
            field[new_row][new_col] = '*'
            print("Alice didn't make it to the tea party.")
            break
        else:
            field[new_row][new_col] = 'A'
            alice_row = new_row
            alice_col = new_col

    else:

        print("Alice didn't make it to the tea party.")
        break

[print(*row) for row in field]
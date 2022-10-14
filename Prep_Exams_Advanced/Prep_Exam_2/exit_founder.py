names = input().split(', ')

rows, cols = 6, 6

board = []

for _ in range(rows):
    board.append(input().split())

skipper = {}

while True:

    player = names[0]
    player_row, player_col = input().lstrip('(').rstrip(')').split(", ")
    player_row = int(player_row)
    player_col = int(player_col)

    if player in skipper:
        if skipper[player] > 0:
            skipper[player] -= 1
            names.append(names.pop(0))
            continue

    if board[player_row][player_col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    if board[player_row][player_col] == 'T':
        print(f"{player} is out of the game! The winner is {names[1]}.")
        break

    if board[player_row][player_col] == 'W':
        if player not in skipper:
            skipper[player] = 1
        else:
            skipper[player] += 1
        print(f"{player} hits a wall and needs to rest.")

        names.append(names.pop(0))
        continue

    names.append(names.pop(0))

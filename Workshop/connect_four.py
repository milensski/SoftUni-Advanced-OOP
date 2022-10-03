def board_print():
    for row in board:
        print(row)


rows, cols = 6, 7

board = []

for r in range(rows):
    row_element = []
    for c in range(cols):
        row_element.append(0)
    board.append(row_element)

board_print()

current_row = (rows - 1)

player = 1

while True:

    current_col = int(input(f'Player {player} please choose a column: '))

    if board[current_row][current_col] == 0:
        board[current_row][current_col] = player

    else:
        while board[current_row][current_col] != 0 and 0 <= current_row < rows:
            current_row -= 1
        board[current_row][current_col] = player

    player += 1

    if player > 2:
        player = 1

    current_row = (rows - 1)
    board_print()

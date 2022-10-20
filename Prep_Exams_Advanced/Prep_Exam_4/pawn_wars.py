

board = []

for i in range(8,-1,-1):
    row = []
    for j in range(8):
        row.append(f'{chr(97+j)}{i}')
    board.append(row)

w=[]
b=[]

for current_row in range(8):
    row_elements = input().split()
    for current_col in range(len(row_elements)):
        if row_elements[current_col] == 'w':
            w = [current_row,current_col,'White']
        elif row_elements[current_col] == 'b':
            b = [current_row,current_col,'Black']

players = [w,b]

while True:


    player_row1,player_col1, name1 = players[0]
    player_row2,player_col2, name2 = players[1]

    if name1 == 'White':
        if (player_row1 - 1 == player_row2 and player_col1 - 1 == player_col2) or (player_row1 - 1 == player_row2 and player_col1 + 1 == player_col2):

            print(f"Game over! {name1} win, capture on {board[player_row2][player_col2]}.")
            break
        else:
            players[0][0] -= 1
            if players[0][0] < 0:
                print(f'Game over! {name1} pawn is promoted to a queen at {board[player_row1][player_col1]}.')
                break

    elif name1 == 'Black':
        if (player_row1 + 1 == player_row2 and player_col1 - 1 == player_col2) or (player_row1 + 1 == player_row2 and player_col1 + 1 == player_col2):

            print(f"Game over! {name1} win, capture on {board[player_row2][player_col2]}.")
            break
        else:
            players[0][0] += 1
            if players[0][0] >= 8:
                print(f'Game over! {name1} pawn is promoted to a queen at {board[player_row1][player_col1]}.')
                break

    players.append(players.pop(0))
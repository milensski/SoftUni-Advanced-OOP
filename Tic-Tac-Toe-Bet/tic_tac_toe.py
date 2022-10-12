import random


def board_print():
    for row in board:
        print(f"| {f' | '.join(map(str, row))} |")


board = []
board_places = {}
rows, cols = 3, 3

counter = 1
for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append({counter:(row,col)})
        counter += 1
    board.append(row_elements)

counter = 1
for row in range(rows):
    for col in range(cols):
        board_places[counter] = [row,col]
        counter += 1

board_print()


bet_for_winner = input('Which player will win (X or O): ')

players = [
    [1, 'X'],
    [2, 'O']
]

choices = set()
while len(choices) != 9:

    player_number, player_symbol = players[0]

    choice = random.randrange(1,10)
    if choice in choices:
        continue
    choices.add(choice)

    place_row,place_col = board_places[choice]

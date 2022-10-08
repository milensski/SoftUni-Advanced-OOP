import os


from colorama import Fore, Back
from pyfiglet import Figlet

def board_print():
    for row in board:
        print(f"{Fore.LIGHTWHITE_EX}[ {f'{Fore.LIGHTWHITE_EX} '.join(map(str, row))} ]")



def in_range(row, col, rows, cols):
    if 0 <= row < rows and 0 <= col < cols:
        return True

    return False


def check_win(board, player_number):
    coordinates = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [-1, 1],
        [-1, -1],
        [1, 1],
        [1, -1]
    ]

    for row in range(rows):
        for col in range(cols):

            if board[row][col] != player_number:
                continue

            for r, c in coordinates:
                next_row, next_col = row + r, col + c

                for i in range(3):

                    if not in_range(next_row, next_col, rows, cols):
                        break
                    if board[next_row][next_col] != player_number:
                        break

                    next_row += r
                    next_col += c

                else:
                    return True

    return False

figlet = Figlet(font='big')

print(figlet.renderText('CONNECT 4'))

rows, cols = 6, 7

board = [["0"] * cols for row in range(rows)]

board_print()

print()

player = 1

while True:
    current_row = (rows - 1)

    try:

        player_number = ''

        if player == 1:
            player_number = Fore.LIGHTYELLOW_EX + str(player) + Fore.RESET
        elif player == 2:
            player_number = Fore.RED + str(player) + Fore.RESET


        current_col = int(input(f'{Fore.RESET}Player {player_number} please choose a column: ')) - 1

        if current_col < 0:
            print(Back.RED + Fore.BLACK + 'Not a valid column!' + Fore.RESET + Back.RESET)
            continue

        if board[current_row][current_col] == '0':
            board[current_row][current_col] = player_number

        else:
            while board[current_row][current_col] != '0' and 0 <= current_row < rows:
                current_row -= 1

            if board[current_row][current_col] == '0':
                board[current_row][current_col] = player_number
            else:
                print(Fore.LIGHTBLUE_EX + 'Column is full !' + Fore.RESET)
                continue

        if check_win(board, player_number):
            board_print()
            print()
            print(f'{Back.GREEN}{Fore.BLACK}Player {player_number} {Fore.BLACK}WINS!{Back.RESET}')
            exit()

        player += 1

        if player > 2:
            player = 1


        # os.system('clear')
        board_print()

    except ValueError:
        print(Back.RED + Fore.BLACK + 'Not a valid input!' + Fore.RESET + Back.RESET)
    except IndexError:
        print(Back.RED + Fore.BLACK + 'Not a valid column!' + Fore.RESET + Back.RESET)

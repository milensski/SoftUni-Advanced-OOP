def get_count_attacks(row,col,size):
    possible_attacks = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]

    result = 0

    for r, c in possible_attacks:
        if (0 <= r < size) and (0 <= c < size):
            if board[r][c] == "K":
                result += 1

    return result

size = int(input())

board = []

for _ in range(size):
    board.append(list(input()))

removed_knights = 0

while True:
    best_score = 0
    knight_row = 0
    knight_col = 0

    for row in range(size):
        for col in range(size):

            if board[row][col] == "0":
                continue

            count = get_count_attacks(row,col,size)

            if count > best_score:
                best_score = count
                knight_row = row
                knight_col = col

    if best_score == 0:
        break

    board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)

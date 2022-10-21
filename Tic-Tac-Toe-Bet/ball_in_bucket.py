

board = []

for _ in range(6):
    board.append(input().split())


score = 0
for _ in range(3):
    row,col = map(int,input().strip('()').split(', '))

    if row < 0 or row >=6 or col < 0 or col >=6:

        continue

    if board[row][col] == 'B':
        board[row][col] = '0'

        for i in range(6):
            if board[i][col].isdigit():
                score += int(board[i][col])

if score < 100:
    print(f"Sorry! You need {100-score} points more to win a prize.")
elif score < 200:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif score < 300:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
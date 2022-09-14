from collections import deque


players = deque(input().split())
n = int(input())
counter = 1
while len(players) > 1:
    player = players.popleft()

    if counter == n:
        counter = 1
        print(f'Removed {player}')
    else:
        players.append(player)
        counter += 1

print(f'Last is {players.popleft()}')
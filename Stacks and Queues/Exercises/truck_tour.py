from collections import deque

N = int(input())

pumps = deque()

for _ in range(N):
    amount, distance = input().split()
    pumps.append([int(amount), int(distance)])

for idx in range(len(pumps)):
    fuel = 0
    failed = False
    for amount, distance in pumps:
        fuel = fuel + amount - distance
        if fuel < 0:
            pumps.append(pumps.popleft())
            failed = True
            break

    if not failed:
        print(idx)
        break


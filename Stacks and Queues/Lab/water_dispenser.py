from collections import deque

quantity = int(input())

que = deque([])

while True:
    name = input()

    if name == 'Start':
        break

    que.append(name)

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'refill':
        liters = int(command[1])
        quantity += liters
    else:
        liters = int(command[0])
        if liters <= quantity:
            quantity -= liters
            person = que.popleft()
            print(f'{person} got water')
        else:
            person = que.popleft()
            print(f'{person} must wait')

print(f'{quantity} liters left')

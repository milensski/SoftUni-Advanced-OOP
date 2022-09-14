from collections import deque


queue = deque()

while True:
    customer = input()

    if customer == 'End':
        break

    if customer == 'Paid':
        while queue:
            name = queue.popleft()
            print(name)
    else:
        queue.append(customer)

print(f'{len(queue)} people remaining.')
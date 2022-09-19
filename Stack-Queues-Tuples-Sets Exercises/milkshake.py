from collections import deque

from collections import deque

chocolates = deque(map(int, input().split(', ')))
cups_milk = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes != 5:

    if chocolates and cups_milk:
        last_chocolate = chocolates[-1]
        cup = cups_milk.popleft()

        if last_chocolate <= 0:
            chocolates.pop()
            if cup <= 0:
                continue
            else:
                cups_milk.appendleft(cup)
                continue
        elif cup <= 0:
            continue

        if last_chocolate == cup:
            milkshakes += 1
            chocolates.pop()
        else:
            cups_milk.append(cup)
            chocolates.pop()
            chocolates.append(last_chocolate - 5)


    else:
        break

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if len(chocolates) > 0:
    print(f'Chocolate: {", ".join(map(str, chocolates))}')
else:
    print('Chocolate: empty')

if len(cups_milk) > 0:
    print(f'Milk: {", ".join(map(str, cups_milk))}')
else:
    print('Milk: empty')


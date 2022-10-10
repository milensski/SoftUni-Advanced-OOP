from collections import deque


seats = input().split(', ')

que = deque(map(int,input().split(', ')))
stack = deque(map(int,input().split(', ')))

rotations = 0

matched_seats = []

while rotations < 10:

    if len(matched_seats) > 3:
        break

    first_element = que.popleft()
    second_element = stack.pop()

    rotations += 1

    letter = chr(sum((first_element,second_element)))

    for seat in seats:
        if letter in seat:
            if first_element == int(seat[:-1]) or second_element == int(seat[:-1]):
                if seat in matched_seats:
                    break
                else:
                    matched_seats.append(seat)
                    break
    else:
        que.append(first_element)
        stack.appendleft(second_element)

    if len(matched_seats) == 3:
        break

print(f'Seat matches: {", ".join(matched_seats)}')
print(f'Rotations count: {rotations}')

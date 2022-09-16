N = int(input())

guests = set()

arrived = set()

for _ in range(N):
    guests.add(input())

while True:

    person = input()

    if person == 'END':
        break

    arrived.add(person)


missing_guests = guests - arrived
print(len(missing_guests))
[print(guest) for guest in sorted(missing_guests)]
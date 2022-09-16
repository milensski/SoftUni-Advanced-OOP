N = int(input())

parking = set()

for _ in range(N):
    direction, plate = input().split(', ')

    if direction == 'IN':
        parking.add(plate)
    elif direction == 'OUT':
        parking.remove(plate)

if len(parking) > 0:
    for plate in parking:
        print(plate)
else:
    print("Parking Lot is Empty")

sequence = tuple(map(float,input().split()))

unique = []

for number in sequence:
    if number not in unique:
        unique.append(number)

for num in unique:
    print(f'{num} - {sequence.count(num)} times')
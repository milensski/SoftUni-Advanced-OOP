from collections import deque

elfs = deque(map(int, input().split()))  # first
materials = deque(map(int, input().split()))  # last

energy = 0
count = 1
toys = 0

while elfs and materials:

    elve = elfs.popleft()
    material = materials.pop()
    toy_made = 0

    if elve < 5:
        materials.append(material)
        continue

    if count % 3 == 0:
        material *= 2

        if elve >= material:
            toys += 2
            toy_made += 2
            elve -= material - 1
            energy += material
            if count % 5 == 0:
                toys -= toy_made
                elve -= 1

        else:
            elfs.append(elve * 2)
            materials.append(int(material / 2))
            count += 1
            continue
    else:

        if elve >= material:
            toys += 1
            toy_made = 1
            elve -= material - 1
            energy += material
            elfs.append(elve)
            if count % 5 == 0:
                toys -= toy_made
                elve -= 1
        else:
            elfs.append(elve * 2)
            materials.append(int(material))
            count += 1
            continue

    count += 1

print(f'Toys: {toys}')
print(f'Energy: {energy}')

if len(elfs) > 0:
    print(f'Elves left: {", ".join(map(str, elfs))}')

if len(materials) > 0:
    print(f'Boxes left: {", ".join(map(str, materials))}')

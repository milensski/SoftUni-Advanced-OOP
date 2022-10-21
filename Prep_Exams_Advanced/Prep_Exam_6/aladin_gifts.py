from collections import deque

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

while materials and magic_levels:

    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    product = current_material + current_magic

    if product < 100:
        if product % 2 == 0:
            current_material *= 2
            current_magic *= 3
            product = current_material + current_magic
        else:
            product *= 2

    elif product > 499:
        product //= 2

    if 100 <= product <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= product <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= product <= 399:
        gifts["Gold"] += 1
    elif 400 <= product <= 499:
        gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) \
        or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if len(materials) > 0:
    print(f"Materials left: {', '.join(map(str, materials))}")
if len(magic_levels) > 0:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")


for item,value in sorted(gifts.items()):
    if value > 0:
        print(f'{item}: {value}')

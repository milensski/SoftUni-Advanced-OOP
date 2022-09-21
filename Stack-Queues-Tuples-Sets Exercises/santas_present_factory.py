from collections import deque

materials = list(map(int, input().split()))  # STACK
magic = deque(map(int, input().split()))

toys = {
    'Doll': {'magic': 150, 'crafted': 0},
    'Wooden train': {'magic': 250, 'crafted': 0},
    'Teddy bear': {'magic': 300, 'crafted': 0},
    'Bicycle': {'magic': 400, 'crafted': 0},
}

while materials and magic:

    is_zero = False
    is_equal = False

    if materials[-1] == 0:
        materials.pop()
        is_zero = True
    if magic[0] == 0:
        magic.popleft()
        is_zero = True

    if is_zero:
        continue

    result = materials[-1] * magic[0]

    if result < 0:
        materials.append(int(materials.pop() + magic.popleft()))
        continue
    else:
        for toy in toys:
            if result == toys[toy]['magic']:
                toys[toy]['crafted'] += 1
                materials.pop()
                magic.popleft()
                is_equal = True
                break
        if not is_equal:
                magic.popleft()
                materials[-1] += 15

if toys['Doll']['crafted'] and toys['Wooden train']['crafted'] \
        > 0 or toys['Teddy bear']['crafted'] and toys['Bicycle']['crafted'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if magic:
    print(f'Magic left: {", ".join(map(str, magic))}')

for toy in sorted(toys):
    if toys[toy]["crafted"] > 0:
        print(f'{toy}: {toys[toy]["crafted"]}')

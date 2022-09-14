stack = input().split()

rack_capacity = int(input())

racks_used = 1

cloth_pieces = 0

for _ in range(len(stack)):

    cloth = int(stack.pop())

    cloth_pieces += cloth

    if rack_capacity == cloth_pieces:
        if len(stack) > 0:
            racks_used += 1
            cloth_pieces = 0
    elif rack_capacity < cloth_pieces:
        racks_used += 1
        cloth_pieces = cloth

    if len(stack) == 0:
        break


print(racks_used)
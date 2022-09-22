rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))


target = input()

found = False

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == target:
            print(f'({row}, {col})')
            found = True
            break
    if found:
        break

if not found:
    print(f"{target} does not occur in the matrix")
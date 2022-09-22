rows = int(input())

even_matrix = []

for row in range(rows):
    even_matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(even_matrix)
rows = int(input())

matrix = []

[matrix.append([int(x) for x in input().split()]) for _ in range(rows)]

primary_diagonal = 0
for i in range(rows):
    primary_diagonal += matrix[i][i]
print(primary_diagonal)
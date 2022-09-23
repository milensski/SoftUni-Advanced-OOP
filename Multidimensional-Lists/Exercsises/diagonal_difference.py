n = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    row = [int(x) for x in input().split(' ')]
    primary_diagonal.append(row[i])
    secondary_diagonal.append(row[len(row) - 1 - i])

difference = abs(sum(primary_diagonal)-sum(secondary_diagonal))

print(difference)
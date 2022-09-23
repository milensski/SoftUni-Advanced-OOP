n = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    row = [int(x) for x in input().split(', ')]
    primary_diagonal.append(row[i])
    secondary_diagonal.append(row[len(row) - 1 - i])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")

rows = int(input())

flatten_matrix = []


[flatten_matrix.extend(int(x) for x in input().split(', ')) for _ in range(rows)]

print(flatten_matrix)
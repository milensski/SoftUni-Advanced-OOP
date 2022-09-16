N = int(input())

sequence = []

[sequence.append(input()) for _ in range(N)]

[print(name) for name in set(sequence)]
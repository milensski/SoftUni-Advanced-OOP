from collections import deque

sequence = deque(map(int, input().split()))
n = int(input())
pairs = []
while len(sequence) > 1:
    num = sequence.popleft()
    for second in sequence:
        if num + second == n:
            pairs.append((num,second))
            sequence.remove(second)
            break
    continue

print(pairs)
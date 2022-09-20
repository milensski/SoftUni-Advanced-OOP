from collections import deque
import operator
bees = deque(map(int,input().split()))
nectar = list(map(int,input().split()))
symbols = deque(input().split())

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

honey = 0

while bees and nectar:

    if bees[0] <= nectar[-1]:
        matched_bee = bees.popleft()
        matched_nectar = nectar.pop()
        symbol = symbols.popleft()
        if matched_nectar == 0:
            continue
        honey += abs(ops[symbol](matched_bee,matched_nectar))
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if len(bees) > 0:
    print(f"Bees left: {', '.join(map(str,bees))}")
if len(nectar) > 0:
    print(f"Nectar left: {', '.join(map(str,nectar))}")
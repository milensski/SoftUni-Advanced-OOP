N = int(input())

collection = set()

for _ in range(N):
    name = input()
    collection.add(name)

[print(name) for name in collection]



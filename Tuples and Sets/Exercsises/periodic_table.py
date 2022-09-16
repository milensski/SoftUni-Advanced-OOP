n = int(input())

unique_compunds = set()


for _ in range(n):
    line = input().split()

    for element in line:
        unique_compunds.add(element)
[print(element) for element in unique_compunds]
N = int(input())

odd_set = set()
even_set = set()

for row in range(1,N+1):
    name = input()
    ascii_sum = 0

    for char in name:
        ascii_sum += ord(char)

    result = ascii_sum // row

    if result % 2 != 0:
        odd_set.add(result)
    else:
        even_set.add(result)


if sum(odd_set) == sum(even_set):
    union = odd_set.union(even_set)
    print(", ".join(map(str,union)))
elif sum(odd_set) > sum(even_set):
    defference = odd_set.difference(even_set)
    print(", ".join(map(str, defference)))
elif sum(odd_set) < sum(even_set):
    symmetric = odd_set.symmetric_difference(even_set)
    print(", ".join(map(str, symmetric)))
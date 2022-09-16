n, m = tuple(map(int, input().split()))

set_n = set()
set_m = set()

for i in range(n + m):

    if i < n:
        set_n.add(int(input()))
    else:
        set_m.add(int(input()))

for element in set_n.intersection(set_m):
    print(element)

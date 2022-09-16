N = int(input())

longest_intersection = {'intersection': [] }

for _ in range(N):

    first, second = input().split('-')

    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')

    set_1 = set()
    set_2 = set()

    for i in range(int(first_start), int(first_end) + 1):
        set_1.add(i)
    for j in range(int(second_start), int(second_end) + 1):
        set_2.add(j)

    intersection = set_1.intersection(set_2)

    if len(intersection) > len(longest_intersection['intersection']):
        longest_intersection['intersection'] = intersection



    set_1.clear()
    set_2.clear()

print(f'Longest intersection is {list(longest_intersection["intersection"])} with length {len(longest_intersection["intersection"])}')

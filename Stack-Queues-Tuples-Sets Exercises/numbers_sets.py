sequence_1 = set(map(int, (input().split())))
sequence_2 = set(map(int, (input().split())))
N = int(input())


def add(working_set, sequence):
    sequence = set(map(int, sequence))

    return working_set.union(sequence)


def remove(working_set, sequence):
    sequence = set(map(int, sequence))

    return working_set.difference(sequence)


for _ in range(N):
    command, position, *sequence = tuple(input().split())

    if position == 'First':
        if command == 'Add':
            sequence_1 = add(sequence_1, sequence)
        elif command == 'Remove':
            sequence_1 = remove(sequence_1, sequence)

    elif position == 'Second':
        if command == 'Add':
            sequence_2 = add(sequence_2, sequence)
        elif command == 'Remove':
            sequence_2 = remove(sequence_2, sequence)

    elif command == 'Check':
        if sequence_1.issubset(sequence_2) or sequence_2.issubset(sequence_1):
            print(True)
        else:
            print(False)

print(', '.join(map(str, sorted(sequence_1))))
print(', '.join(map(str, sorted(sequence_2))))

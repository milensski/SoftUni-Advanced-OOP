from itertools import permutations


def possible_permutations(possibles):
    for permutation in list(permutations(possibles)):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]

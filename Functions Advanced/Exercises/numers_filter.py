def even_odd_filter(**kwargs):
    even_odd = {}

    for key, value in kwargs.items():
        if key == 'odd':
            even_odd[key] = list(filter(lambda x: x % 2 != 0, value))
        else:
            even_odd[key] = list(filter(lambda x: x % 2 == 0, value))

    return dict(sorted(even_odd.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

def sorting_cheeses(**kwargs):

    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]),x[0]))
    result = ''
    for key, value in sorted_cheeses:
        result += key + '\n'
        sorted_values = sorted(value, reverse=True)
        result += '\n'.join(map(str,sorted_values)) + '\n'

    return result




print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

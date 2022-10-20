def start_spring(**kwargs):
    categories = {}
    result = ''
    for name, categorie in kwargs.items():
        if categorie not in categories:
            categories[categorie] = [name]
        else:
            categories[categorie].append(name)

    for k, v in sorted(categories.items(), key=lambda x: (-len(x[1]), x[0])):
        result += k+":"+"\n"
        for element in sorted(v):
            result += f'-{element}\n'

    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))



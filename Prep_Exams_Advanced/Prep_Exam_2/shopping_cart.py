def shopping_cart(*args):

    meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    result = ''

    for arg in args:
        if arg == 'Stop':
            break

        meal, product = arg

        if product in meals[meal]:
            continue

        if meal == 'Soup':

            if len(meals[meal]) < 3:
                meals[meal].append(product)

        elif meal == 'Pizza':
            if len(meals[meal]) < 4:
                meals[meal].append(product)

        elif meal == 'Dessert':
            if len(meals[meal]) < 2:
                meals[meal].append(product)

    if len(meals['Soup']) == 0 and len(meals['Pizza']) == 0 and len(meals['Dessert']) == 0:
        result = 'No products in the cart!'
    else:
        for item in sorted(meals.items(), key= (lambda x: (-len(x[1]),x[0]))):
            result += f'{item[0]+ ":"}\n'
            for element in sorted(item[1]):
                result += f'{" - " + element}\n'

    return result



print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

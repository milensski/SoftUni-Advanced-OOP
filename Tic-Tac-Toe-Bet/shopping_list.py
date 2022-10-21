def shopping_list(budget, **kwargs):
    if budget < 100:
        return f'You do not have enough budget.\n'
    products = 0
    result = ''
    for item, values in kwargs.items():
        price = float(values[0])
        quantity = int(values[1])
        total_price = price * quantity

        if total_price <= budget and products < 5:
            budget -= total_price
            products += 1

            result += f'You bought {item} for {total_price:.2f} leva.\n'

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

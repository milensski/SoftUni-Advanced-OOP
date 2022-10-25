from collections import deque

milligrams_caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

maximum = 300
stamat_caffein = 0

while milligrams_caffeine and energy_drinks:

    last_mg = milligrams_caffeine.pop()
    drink = energy_drinks.popleft()

    caffeine_in_drink = last_mg * drink

    if stamat_caffein + caffeine_in_drink <= 300:
        stamat_caffein += caffeine_in_drink

    elif stamat_caffein + caffeine_in_drink > 300:
        energy_drinks.append(drink)
        stamat_caffein -= 30
        if stamat_caffein < 0:
            stamat_caffein = 0

if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f"Stamat is going to sleep with {stamat_caffein} mg caffeine.")

THis is  a test
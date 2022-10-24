def forecast(*args):
    locations = {}
    result = ''

    for location, weather in args:
        id = 0

        if weather == "Sunny":
            id = 1
        elif weather == "Cloudy":
            id = 2
        elif weather == "Rainy":
            id = 3

        if id not in locations:
            locations[id] = {weather : [location]}
        else:

            locations[id][weather].append(location)

    for key, value in sorted(locations.items()):
        for k, v in sorted(value.items()):
            for loc in sorted(v):
                result += f'{loc} - {k}\n'

    return result



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

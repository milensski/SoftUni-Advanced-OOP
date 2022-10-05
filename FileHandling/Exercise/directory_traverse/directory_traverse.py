from os import listdir


path = './resources/Example'

directories = listdir(path)

extenstions = {}


for directory in directories:
    name, ext = directory.split('.')

    if ext not in extenstions:
        extenstions[ext] = [f"{name}.{ext}"]
    else:
        extenstions[ext].append(f"{name}.{ext}")

content = ''

for key, value in sorted(extenstions.items()):
    content += f'.{key}\n'
    for v in sorted(value):
        content += f'- - - {v}\n'

print(content)

with open("report.txt", 'w') as file:
    file.write(content)


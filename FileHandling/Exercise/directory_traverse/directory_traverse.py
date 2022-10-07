from os import listdir, path, walk

input_path = input('Select root directory to traverse: ')

files = listdir(input_path)

extenstions = {}

for file in files:

    if path.isdir(path.join(input_path,file)):  # statement to exclude zero-level files

        for root, dirs, sub_files in walk(path.join(input_path,file)):

            if sub_files:

                for f in sub_files:
                    name, ext = f.split('.')

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
